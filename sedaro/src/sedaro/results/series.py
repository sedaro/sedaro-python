import dask.dataframe as dd
import json
from functools import cached_property
import os
from pathlib import Path
from typing import Union

from scipy.interpolate import interp1d

try:
    import matplotlib.pyplot as plt
except ImportError:
    PLOTTING_ENABLED = False
else:
    PLOTTING_ENABLED = True

from .utils import HFILL, bsearch, hfill, FromFileAndToFileAreDeprecated


class SedaroSeries(FromFileAndToFileAreDeprecated):

    def __init__(self, name, data):
        '''Initialize a new time series.

        Series are typically created through the .<VARIABLE_NAME> attribute or
        .variable method of SedaroBlockResult or the .from_file method of
        this class.
        '''
        self.__name = name
        try:
            self.__mjd = data.index.values.compute()
        except AttributeError: # used for model_at, in which mjd has already been computed
            self.__mjd = data.index.values
        self.__elapsed_time = [86400 * (entry - self.__mjd[0]) for entry in self.__mjd]
        self.__static_series = data
        self.__series = data.copy()
        self.__has_subseries = len(self.__series.columns.tolist()) > 1
        if self.__has_subseries:
            # rename columns to remove top-level name
            renamed_columns = {}
            for column_name in self.__series.columns.tolist():
                renamed_columns[column_name] = '.'.join(column_name.split('.')[1:])
            self.__series = self.__series.rename(columns=renamed_columns)
            self.__dtype = self.__series.dtypes.to_dict()
        else:
            self.__column_name = self.__series.columns.tolist()[0]
            self.__dtype = self.__series.dtypes.iloc[0]

    def __repr__(self):
        return f"Series({self.name})"

    @property
    def __prepped_nested_series(self):
        '''Prepare nested series for iteration.'''

        def dict_to_list(d):
            if isinstance(d, dict):
                return [dict_to_list(d[i]) for i in sorted(d)]
            return d

        if not self.__has_subseries:
            raise ValueError('This series has no subseries.')
        else:
            # get column names
            columns = {}
            for column_name in self.__series.columns.tolist():
                columns[column_name] = self.__series[column_name].compute().tolist()
            result = []
            for i in range(len(self.__mjd)):
                this_entry = {}
                for column in columns:
                    column_value = columns[column][i]
                    indices = [int(x) for x in column.split('.')]
                    current_level = this_entry
                    for j in indices[:-1]:
                        current_level = current_level.setdefault(j, {})
                    current_level[indices[-1]] = column_value
                result.append(dict_to_list(this_entry))
            return result

    def __iter__(self):
        '''Iterate through time, value pairs in this series.

        Only a series with no subseries is iterable.
        '''
        if self.__has_subseries:
            if not self.__all_subseries_are_numeric:
                raise ValueError('Select a specific subseries to iterate over.')
            else:
                return (entry for entry in zip(self.__mjd, self.__elapsed_time, self.__prepped_nested_series))
        return (entry for entry in zip(self.__mjd, self.__elapsed_time, self.__series[self.__column_name].compute()))

    def __len__(self) -> int:
        return len(self.mjd)

    def __getitem__(self, subseries_name: str):
        '''Get a particular subseries by name.

        Typically invoked by indexing [<SUBSERIES_NAME>] on an instance
        of SedaroSeries. Can only be called if the series has subseries.
        '''
        if not self.__has_subseries:
            raise ValueError('This series has no subseries.')
        else:
            matching_columns = [column for column in self.__series.columns.tolist() if column.split('.')[0] == subseries_name]
            if len(matching_columns) == 0:
                raise ValueError(f"Subseries '{subseries_name}' not found.")
            else:
                return SedaroSeries(f'{self.__name}.{subseries_name}', self.__series[matching_columns])

    def __getattr__(self, subseries_name: str):
        '''Get a particular subseries by name as an attribute.'''
        return self[subseries_name]

    @property
    def name(self):
        return self.__name

    @property
    def elapsed_time(self):
        return self.__elapsed_time

    @property
    def mjd(self):
        return self.__mjd.tolist()

    @property
    def values(self):
        try:
            return self.__series.values.compute().tolist()
        except AttributeError: # used for model_at, in which values have already been computed for the row in question
            return self.__series.values.tolist()

    @cached_property
    def values_interpolant(self):
        return interp1d(self.__mjd.tolist(), self.__series.iloc[:, 0].compute().tolist())

    @property
    def duration(self):
        return (self.mjd[-1] - self.mjd[0]) * 86400

    def value_at(self, mjd, interpolate=False):
        '''Get the value of this series at a particular time in mjd.'''
        if self.__has_subseries:
            subseries_prefixes = set()
            for column in self.__series.columns.tolist():
                subseries_prefixes.add(column.split('.')[0])
            subseries_prefixes = list(subseries_prefixes)
            if self.__all_subseries_are_numeric():
                arr_len = max([int(p) for p in subseries_prefixes]) + 1
                result = [None] * arr_len
                for i in range(arr_len):
                    if (p := str(i)) in subseries_prefixes:
                        result[i] = self.__getattr__(p).value_at(mjd, interpolate=interpolate)
                return result
            else:
                return {key: self.__getattr__(key).value_at(mjd, interpolate=interpolate) for key in subseries_prefixes}
        else:
            def raise_error():
                raise ValueError(f"MJD {mjd} not found in series with bounds [{self.__mjd[0]}, {self.__mjd[-1]}].")
            if mjd < self.__mjd[0] or mjd > self.__mjd[-1]:
                raise_error()
            if not interpolate:
                index = bsearch(self.__mjd, mjd)
                if index < 0:
                    raise_error()
            else:
                return self.values_interpolant(mjd)
            return self.__series.head(index + 1).tail(1).values[0][0]

    def plot(self, show=True, ylabel=None, elapsed_time=True, height=None, xlim=None, ylim=None, **kwargs):
        self.__plot(show, ylabel, elapsed_time, height, xlim, ylim, **kwargs)

    # def scatter(self, **kwargs):
    #     # TODO: Does not work with 2D value arrays
    #     show = kwargs.pop('show', True)
    #     self.__plot(plt.scatter, show, kwargs)

    def __all_subseries_are_numeric(self):
        subseries = self.__series.columns.tolist()
        for column in subseries:
            for ch in column:
                if ch not in '0123456789.':
                    return False
        else:
            return True

    def __plot(self, show, ylabel, elapsed_time, height, xlim, ylim, **kwargs):
        if not PLOTTING_ENABLED:
            raise ValueError('Plotting is disabled because matplotlib could not be imported.')
        if self.__has_subseries and not self.__all_subseries_are_numeric():
            raise ValueError('Select a specific subseries to plot.')
        try:
            if height is not None:
                plt.rcParams['figure.figsize'] = [plt.rcParams['figure.figsize'][0], height]
            plt.plot((self.__elapsed_time if elapsed_time else self.__mjd), self.values, **kwargs)
            if 'label' in kwargs:
                plt.legend(loc='upper left')
            plt.xlabel('Elapsed Time (s)' if elapsed_time else 'Time (MJD)')
            plt.ylabel(ylabel)
            if xlim:
                plt.xlim(xlim)
            if ylim:
                plt.ylim(ylim)
            if show:
                plt.show()
        except Exception:
            raise ValueError(
                "The data type of this series does not support plotting or the keyword arguments passed were unrecognized.")

    def save(self, path: Union[str, Path]):
        '''Save the series result to a directory with the specified path.'''
        try:
            os.makedirs(path)
        except FileExistsError:
            if not (os.path.isdir(path) and any(os.scandir(path))):
                raise FileExistsError(f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': 'SedaroSeries'}, fp)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump({'name': self.__name}, fp)
        self.__static_series.to_parquet(f"{path}/data.parquet")
        print(f"Series result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load a series result from the specified path.'''
        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SedaroSeries':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            name = json.load(fp)['name']
        data = dd.read_parquet(f"{path}/data.parquet")
        return cls(name, data)

    def summarize(self):
        hfill()
        print("Sedaro Simulation Series Summary".center(HFILL))
        print(f"'{self.name}'".center(HFILL))
        hfill()
        average_step = self.duration / len(self.elapsed_time)
        print(f"📈 {len(self)} points covering {self.duration/60:.1f} minutes with ~{average_step:.1f}s steps")

        if self.__has_subseries:
            print("\n📑 This series has subseries.")
            print(f"\n🗂️ Value data types are:")
            for key, value in self.__dtype.items():
                if value == 'None':
                    print(f"    - '{key}': All entries in this subseries are None")
                else:
                    print(f"    - '{key}': '{value}'")

        else:
            if self.__dtype == 'None':
                print('\n⛔ All entries in this series are None')
            else:
                print(f"\n🗂️ Value data type is '{self.__dtype}'")

        hfill()
        if self.__has_subseries:
            print("❓ Index [<SUBSERIES_NAME>] to select a subseries")
        else:
            print("❓ Call .plot to visualize results")
