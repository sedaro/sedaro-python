import dask.dataframe as dd
import json
from functools import cached_property
import numpy as np
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

from .utils import HFILL, bsearch, get_column_names, hfill, FromFileAndToFileAreDeprecated


class SedaroSeries(FromFileAndToFileAreDeprecated):

    def __init__(self, name, data, column_index, prefix):
        '''Initialize a new time series.

        Series are typically created through the .<VARIABLE_NAME> attribute or
        .variable method of SedaroBlockResult or the .from_file method of
        this class.
        '''
        self.__name = name
        self.__prefix = prefix
        self.__column_index = column_index
        self.__has_subseries = len(self.__column_index) > 0
        self.__column_names = get_column_names(self.__column_index, self.__prefix)
        try:
            self.__mjd = data.index.values.compute()
        except AttributeError: # used for model_at, in which mjd has already been computed
            self.__mjd = data.index.values
        self.__elapsed_time = [86400 * (entry - self.__mjd[0]) for entry in self.__mjd]
        self.__series = data[self.__column_names]
        if self.__has_subseries:
            self.__dtype = self.__series.dtypes.to_dict()
        else:
            self.__dtype = self.__series.dtypes.iloc[0]

    def __repr__(self):
        return f"Series({self.name})"

    def __is_singleton_or_vector(self):
        for column_name in self.__column_names:
            for ch in column_name[len(self.__prefix):]:
                if ch not in '0123456789.':
                    return False
        return True

    def __iter__(self):
        '''Iterate through time, value pairs in this series.

        Only a series with no subseries is iterable.
        '''
        if (self.__has_subseries and not self.__is_singleton_or_vector()):
            raise ValueError('Select a specific subseries to iterate over.')
        else:
            return (entry for entry in zip(self.__mjd, self.__elapsed_time, self.values))

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
            if subseries_name not in self.__column_index:
                raise ValueError(f"Subseries '{subseries_name}' not found.")
            else:
                return SedaroSeries(f'{self.__name}.{subseries_name}', self.__series, self.__column_index[subseries_name], f'{self.__prefix}.{subseries_name}')

    def __getattr__(self, subseries_name: str):
        '''Get a particular subseries by name as an attribute.'''
        return self[subseries_name]

    @property
    def dataframe(self) -> dd.DataFrame:
        '''Get the raw Dask DataFrame for this series.'''
        return self.__series

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
        if not (self.__has_subseries and not self.__is_singleton_or_vector()):
            if not self.__has_subseries:
                return self.__series[self.__column_names[0]].compute().tolist()
            else:
                computed_columns = {column_name: self.__series[column_name].compute().tolist() for column_name in self.__series.columns}
                vals = []
                for column in computed_columns:
                    indexes = [int(x) for x in column.split('.')]
                    ptr = vals
                    for index in indexes:
                        if len(ptr) == index:
                            ptr.append([])
                        elif len(ptr) < index:
                            ptr.extend([[] for _ in range(index - len(ptr))])
                        ptr = ptr[index]
                    ptr.extend(computed_columns[column])
                return np.transpose(vals, axes=None).tolist()

        else:
            return {key: self.__getattr__(key).values for key in self.__column_index}

    @cached_property
    def values_interpolant(self):
        return interp1d(self.__mjd.tolist(), self.__series.iloc[:, 0].compute().tolist())

    @property
    def duration(self):
        return (self.mjd[-1] - self.mjd[0]) * 86400

    def value_at(self, mjd, interpolate=False):
        '''Get the value of this series at a particular time in mjd.'''
        if self.__has_subseries:
            if not self.__is_singleton_or_vector():
                return {key: self.__getattr__(key).value_at(mjd, interpolate=interpolate) for key in self.__column_index}
            else:
                arr_len = max([int(i) for i in self.__column_index]) + 1
                result = [None] * arr_len
                for i in range(arr_len):
                    if (k := str(i)) in self.__column_index: # in case it has 0, 1, 3, but not 2, etc.
                        result[i] = self.__getattr__(k).value_at(mjd, interpolate=interpolate)
                return result
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
                return self.values_interpolant(mjd).tolist() # casts from nparr(x) to x
            return self.__series.head(index + 1).tail(1).values[0][0]

    def plot(self, show=True, ylabel=None, elapsed_time=True, height=None, xlim=None, ylim=None, **kwargs):
        self.__plot(show, ylabel, elapsed_time, height, xlim, ylim, **kwargs)

    # def scatter(self, **kwargs):
    #     # TODO: Does not work with 2D value arrays
    #     show = kwargs.pop('show', True)
    #     self.__plot(plt.scatter, show, kwargs)

    def __plot(self, show, ylabel, elapsed_time, height, xlim, ylim, **kwargs):
        if not PLOTTING_ENABLED:
            raise ValueError('Plotting is disabled because matplotlib could not be imported.')
        if self.__has_subseries and not self.__is_singleton_or_vector():
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
            json.dump({
                'name': self.__name,
                'column_index': self.__column_index,
                'prefix': self.__prefix,
            }, fp)
        self.__series.to_parquet(f"{path}/data.parquet")
        print(f"Series result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load a series result from the specified path.'''
        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SedaroSeries':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            meta = json.load(fp)
            name = meta['name']
            column_index = meta['column_index']
            prefix = meta['prefix']
        data = dd.read_parquet(f"{path}/data.parquet")
        return cls(name, data, column_index, prefix)

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
                name_without_prefix = key[len(self.__prefix)+1:]
                if value == 'None':
                    print(f"    - '{name_without_prefix}': All entries in this subseries are None")
                else:
                    print(f"    - '{name_without_prefix}': '{value}'")

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
