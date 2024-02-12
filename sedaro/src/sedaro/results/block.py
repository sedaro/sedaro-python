import dask.dataframe as dd
import gzip
import json
import os
from pathlib import Path
import shutil
from typing import Generator, Union
import uuid6

from .series import SedaroSeries
from .utils import ENGINE_EXPANSION, ENGINE_MAP, HFILL, hfill


class SedaroBlockResult:

    def __init__(self, structure, series: dict):
        '''Initialize a new block result.

        Block results are typically created through the .block method of
        SedaroAgentResult or the .from_file method of this class.
        '''
        if 'name' in structure:
            self.__name = structure['name']
        elif structure == 'root':
            self.__name = 'root'
        else:
            self.__name = '<Unnamed Block>'
        self.__structure = structure
        self.__series = series
        
        self.__variables = set()
        for module in self.__series:
            to_rename = {}
            for column_name in self.__series[module].columns.tolist():
                if column_name.split('.')[0] == module:
                    # rename to engine name
                    module_name = ENGINE_EXPANSION[ENGINE_MAP[module.split('/')[1]]]
                    self.__variables.add(module_name)
                    new_column_name = f"{module_name}.{'.'.join(column_name.split('.')[1:])}"
                    to_rename[column_name] = new_column_name
                else:
                    self.__variables.add(column_name.split('.')[0])
            if len(to_rename) > 0:
                self.__series[module] = self.__series[module].rename(columns=to_rename)
        self.__variables = sorted(list(self.__variables))

    def __getattr__(self, name: str) -> SedaroSeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        for module in self.__series:
            selected_columns = []
            for column_name in self.__series[module].columns.tolist():
                if column_name.split('.')[0] == name:
                    selected_columns.append(column_name)
            if len(selected_columns) > 0:
                variable_dataframe = self.__series[module][selected_columns]
                return SedaroSeries(name, variable_dataframe)
        else:
            raise ValueError(f'Variable "{name}" not found.')

    def __contains__(self, variable: str) -> bool:
        '''Check if this block contains a variable by name.'''
        return variable in self.variables

    def __iter__(self) -> Generator:
        '''Iterate through variables on this block.'''
        return (self.__getattr__(variable) for variable in self.variables)

    def __repr__(self) -> str:
        return f'SedaroBlockResult({self.name})'

    @property
    def name(self):
        return self.__name

    @property
    def modules(self):
        return self.__series.keys()

    @property
    def variables(self):
        return self.__variables

    def module_to_dataframe(self):
        raise NotImplementedError("")

    def variable(self, name: str) -> SedaroSeries:
        '''Query a particular variable by name.'''
        return self.__getattr__(name)

    def save(self, filename: Union[str, Path]):
        success = False
        try:
            tmpdir = f".{uuid6.uuid7()}"
            os.mkdir(tmpdir)
            with open(f"{tmpdir}/structure.json", "w") as fp:
                json.dump(self.__structure, fp)
            os.mkdir(f"{tmpdir}/data")
            for engine in self.__series:
                path = f"{tmpdir}/data/{engine.replace('/', ' ')}"
                df : dd = self.__series[engine]
                df.to_parquet(path)
            shutil.make_archive(tmpzip := f".{uuid6.uuid7()}", 'zip', tmpdir)
            curr_zip_base = ''
            # if the path is to another directory, make that directory if nonexistent, and move the zip there
            if len(path_split := filename.split('/')) > 1:
                path_dirs = '/'.join(path_split[:-1])
                Path(path_dirs).mkdir(parents=True, exist_ok=True)
                shutil.move(f"{tmpzip}.zip", f"{(curr_zip_base := path_dirs)}/{tmpzip}.zip")
                zip_desired_name = path_split[-1]
            else:
                zip_desired_name = filename
            # rename zip to specified name
            if len(curr_zip_base) > 0:
                zip_new_path = f"{curr_zip_base}/{zip_desired_name}"
                curr_zip_name = f"{curr_zip_base}/{tmpzip}"
            else:
                zip_new_path = zip_desired_name
                curr_zip_name = tmpzip
            shutil.move(f"{curr_zip_name}.zip", zip_new_path)
            # remove tmpdir
            shutil.rmtree(tmpdir, ignore_errors=True)
            success = True
            print(f"Successfully archived at {zip_new_path}")
        except Exception as e:
            raise e
        finally:
            if not success:
                shutil.rmtree(tmpdir, ignore_errors=True)

    @classmethod
    def load(cls, filename: Union[str, Path]):
        success = False
        try:
            tmpdir = f".{uuid6.uuid7()}"
            shutil.unpack_archive(filename, tmpdir, 'zip')
            with open(f"{tmpdir}/structure.json", "r") as fp:
                structure = json.load(fp)
            engines = {}
            parquets = os.listdir(f"{tmpdir}/data/")
            for agent in parquets:
                df = dd.read_parquet(f"{tmpdir}/data/{agent}")
                engines[agent.replace(' ', '/')] = df
            # remove tmpdir
            shutil.rmtree(tmpdir, ignore_errors=True)
            success = True
        except Exception as e:
            raise e
        finally:
            if not success:
                shutil.rmtree(tmpdir, ignore_errors=True)
        return SedaroBlockResult(structure, engines)

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print("Sedaro Simulation Block Result Summary".center(HFILL))
        if self.name != '<Unnamed Block>':
            print(f"'{self.name}'".center(HFILL))
        hfill()

        print("🧩 Simulated Modules")
        for module in self.modules:
            print(f'    • {ENGINE_EXPANSION[ENGINE_MAP[module.split("/")[1]]]}')

        print("\n📋 Variables Available")
        for variable in self.variables:
            print(f'    • {variable}')
        hfill()
        print("❓ Query variables with .<VARIABLE_NAME>")

    def value_at(self, mjd):
        return {variable: self.__getattr__(variable).value_at(mjd) for variable in self.variables}
