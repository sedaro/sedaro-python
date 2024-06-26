import copy
import json
import os
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Union

from .utils import (HFILL, FromFileAndToFileAreDeprecated, bsearch,
                    get_column_names, hfill)

if TYPE_CHECKING:
    import dask.dataframe as dd

class SedaroSeries(FromFileAndToFileAreDeprecated):

    def __init__(self, name, data, stats, column_index, prefix, stats_to_plot: list = None, block_name: str = None):
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
        self.__block_name = block_name if block_name != '<Unnamed Block>' else None
        try:
            self.__mjd = data.index.values.compute()
        except AttributeError:  # used for model_at, in which mjd has already been computed
            self.__mjd = data.index.values
        self.__elapsed_time = [86400 * (entry - self.__mjd[0]) for entry in self.__mjd]
        self.__series = data[self.__column_names]
        self.__initial_stats = copy.deepcopy(stats)
        self.__stats = {}
        for k in stats:
            if k == prefix or k.startswith(prefix + '.'):
                self.__stats[k] = stats[k]
        if self.__has_subseries:
            self.__dtype = self.__series.dtypes.to_dict()
        else:
            self.__dtype = self.__series.dtypes.iloc[0]
        self.stats_to_plot = stats_to_plot if stats_to_plot is not None else []

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
            if type(subseries_name) is int:
                subseries_name = str(subseries_name)
            if subseries_name not in self.__column_index:
                raise ValueError(f"Subseries '{subseries_name}' not found.")
            else:
                return SedaroSeries(
                    f'{self.__name}.{subseries_name}',
                    self.__series,
                    self.__stats,
                    self.__column_index[subseries_name],
                    f'{self.__prefix}.{subseries_name}',
                    stats_to_plot=self.stats_to_plot,
                    block_name=self.__block_name
                )

    def __getattr__(self, subseries_name: str):
        '''Get a particular subseries by name as an attribute.'''
        return self[subseries_name]

    @property
    def dataframe(self) -> 'dd.DataFrame':
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
        def nonprefixed_column_name(column_name):
            if len(self.__prefix) > 0:
                return column_name[len(self.__prefix) + 1:]
            else:
                return column_name

        if not (self.__has_subseries and not self.__is_singleton_or_vector()):
            if not self.__has_subseries:
                return self.__series[self.__column_names[0]].compute().tolist()
            else:
                computed_columns = {nonprefixed_column_name(
                    column_name): self.__series[column_name].compute().tolist() for column_name in self.__series.columns}
                vals = []
                num_indexes = -1
                for column in computed_columns:
                    indexes = [int(x) for x in column.split('.')]
                    if num_indexes == -1:
                        num_indexes = len(indexes)
                    ptr = vals
                    for index in indexes:
                        if len(ptr) == index:
                            ptr.append([])
                        elif len(ptr) < index:
                            ptr.extend([[] for _ in range(index - len(ptr))])
                        ptr = ptr[index]
                    ptr.extend(computed_columns[column])
                rotated_indexes = tuple([num_indexes] + list(range(num_indexes)))
                import numpy as np
                return np.transpose(vals, rotated_indexes).tolist()

        else:
            return {key: self.__getattr__(key).values for key in self.__column_index}

    @cached_property
    def values_interpolant(self):
        import numpy as np
        from scipy.interpolate import interp1d
        return interp1d(self.mjd, np.asarray(self.values).T)

    @property
    def duration(self):
        return (self.mjd[-1] - self.mjd[0]) * 86400

    def subst_name(self, key):
        if self.__block_name is None:
            return key
        else:
            return '.'.join([self.__block_name] + key.split('.')[1:])

    def stats(self, *args):
        if not self.__has_subseries:
            if len(args) == 0:
                return self.__stats[self.__prefix]
            elif len(args) == 1:
                return self.__stats[self.__prefix][args[0]]
            else:
                return tuple(self.__stats[self.__prefix][k] for k in args)
        else:
            cutoff_len = len(self.__prefix) + 1
            if len(args) == 0:
                return {k[cutoff_len:]: self.__stats[k] for k in self.__stats}
            elif len(args) == 1:
                return {k[cutoff_len:]: self.__stats[k][args[0]] for k in self.__stats}
            else:
                dicts_to_return = []
                for arg in args:
                    dicts_to_return.append({k[cutoff_len:]: self.__stats[k][arg] for k in self.__stats})
                return tuple(dicts_to_return)

    def plot_stats(self, show=True, xlabel=None):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            raise ValueError('Plotting is disabled because matplotlib could not be imported.')
        try:
            if self.__has_subseries and not self.__is_singleton_or_vector():
                raise ValueError('Select a specific subseries to plot.')
            else:
                if not self.__stats:
                    raise ValueError('No statistics available to plot.')
                else:
                    position = len(self.stats_to_plot)
                    self.stats_to_plot.append({
                        'label': xlabel if xlabel is not None else self.subst_name(self.__prefix),
                        'min': self.__stats[self.__prefix]['min'],
                        'max': self.__stats[self.__prefix]['max'],
                        'avg': self.__stats[self.__prefix]['average'],
                        'pos': position,
                    })
                    if show:
                        for box in self.stats_to_plot:
                            plt.plot([box['pos'], box['pos']], [box['min'], box['max']], color='black', linewidth=1.5)
                            plt.plot([box['pos'] - 0.3, box['pos'] + 0.3], [box['min'], box['min']], color='black', linewidth=1.5)
                            plt.plot([box['pos'] - 0.3, box['pos'] + 0.3], [box['max'], box['max']], color='black', linewidth=1.5)
                            plt.plot([box['pos'] - 0.3, box['pos'] + 0.3], [box['avg'], box['avg']], color='#2D56A0', linestyle='dotted', linewidth=1.5)
                        plt.xticks([box['pos'] for box in self.stats_to_plot], [box['label'] for box in self.stats_to_plot], rotation=15)
                        plt.tight_layout()
                        plt.show()
                        self.stats_to_plot.clear()
        except:
            raise ValueError('The data of this series do not have the necessary statistics to plot.')

    def value_at(self, mjd, interpolate=False):
        '''Get the value of this series at a particular time in mjd.'''
        if self.__has_subseries:
            if not self.__is_singleton_or_vector():
                return {key: self.__getattr__(key).value_at(mjd, interpolate=interpolate) for key in self.__column_index}
            else:
                arr_len = max([int(i) for i in self.__column_index]) + 1
                result = [None] * arr_len
                for i in range(arr_len):
                    if (k := str(i)) in self.__column_index:  # in case it has 0, 1, 3, but not 2, etc.
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
                return self.values_interpolant(mjd).tolist()  # casts from nparr(x) to x
            return self.__series.head(index + 1).tail(1).values[0][0]

    def plot(self, show=True, ylabel=None, elapsed_time=True, height=None, xlim=None, ylim=None, **kwargs):
        self.__plot(show, ylabel, elapsed_time, height, xlim, ylim, **kwargs)

    # def scatter(self, **kwargs):
    #     # TODO: Does not work with 2D value arrays
    #     show = kwargs.pop('show', True)
    #     self.__plot(plt.scatter, show, kwargs)

    def __plot(self, show, ylabel, elapsed_time, height, xlim, ylim, **kwargs):
        try:
            import matplotlib.pyplot as plt
        except ImportError:
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
                raise FileExistsError(
                    f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': 'SedaroSeries'}, fp)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump({
                'name': self.__name,
                'column_index': self.__column_index,
                'prefix': self.__prefix,
                'stats': self.__initial_stats,
                'block_name': self.__block_name,
            }, fp)
        self.__series.to_parquet(f"{path}/data.parquet")
        print(f"Series result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load a series result from the specified path.'''
        import dask.dataframe as dd

        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SedaroSeries':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            meta = json.load(fp)
            name = meta['name']
            column_index = meta['column_index']
            prefix = meta['prefix']
            stats = meta['stats'] if 'stats' in meta else {}
            block_name = meta['block_name'] if 'block_name' in meta else None
        data = dd.read_parquet(f"{path}/data.parquet")
        return cls(name, data, stats, column_index, prefix, block_name=block_name)

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
                stats_marker = '\033[0;32m*\033[0;0m' if key in self.__stats else ' '
                name_without_prefix = key[len(self.__prefix) + 1:]
                if value == 'None':
                    print(f"    - {stats_marker} '{name_without_prefix}': All entries in this subseries are None")
                else:
                    print(f"    - {stats_marker} '{name_without_prefix}': '{value}'")

        else:
            if self.__dtype == 'None':
                print('\n⛔ All entries in this series are None')
            else:
                print(f"\n🗂️ Value data type is '{self.__dtype}'")
            if self.__stats:
                print('\n📊 Statistics:')
                for k in self.__stats[self.__prefix]:
                    print(f"    - {k}: {self.__stats[self.__prefix][k]}")

        hfill()
        if self.__has_subseries:
            print("❓ Index [<SUBSERIES_NAME>] to select a subseries")
            print("❓ Query statistics with [<SUBSERIES_NAME>].stats('<STAT_NAME_1>', '<STAT_NAME_2>', ...)")
            print("📊 Variables with statistics available are marked with a \033[0;32m*\033[0;0m")
        else:
            print("❓ Call .plot to visualize results")
            print("❓ Call .plot_stats to visualize statistics")
