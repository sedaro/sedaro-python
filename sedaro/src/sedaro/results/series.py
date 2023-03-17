import gzip
import json

try:
    import matplotlib.pyplot as plt
except ImportError:
    PLOTTING_ENABLED = False
else:
    PLOTTING_ENABLED = True

from sedaro.results.utils import _get_series_type, hfill, HFILL


class SedaroSeries:

    def __init__(self, name, time, series):
        '''Initialize a new time series.

        Series are typically created through the .<VARIABLE_NAME> attribute or
        .variable method of SedaroBlockResult or the .from_file method of
        this class.
        '''
        self.__name = name
        self.__mjd = time
        self.__elapsed_time = [86400 * (entry - self.__mjd[0]) for entry in self.__mjd]
        self.__series = series
        self.__has_subseries = isinstance(self.__series, dict)
        if self.__has_subseries:
            self.__dtype = {key: _get_series_type(subseries) for key, subseries in self.__series.items()}
        else:
            self.__dtype = _get_series_type(series)

    def __repr__(self):
        return f"Series({self.name})"

    def __iter__(self):
        '''Iterate through time, value pairs in this series.

        Only a series with no subseries is iterable.
        '''
        if self.__has_subseries:
            raise ValueError('Select a specific subseries to iterate over.')
        return (entry for entry in zip(self.__elapsed_time, self.__series))

    def __getattr__(self, subseries_name: str):
        '''Get a particular subseries by name.

        Typically invoked by calling .<SUBSERIES_NAME> on an instance
        of SedaroSeries. Can only be called if the series has subseries.
        '''
        if not self.__has_subseries:
            raise ValueError('This series has no subseries.')
        elif subseries_name in self.__series:
            new_series_name = f'{self.__name}.{subseries_name}'
            return SedaroSeries(new_series_name, self.__mjd, self.__series[subseries_name])
        else:
            raise ValueError(f"Subseries '{subseries_name}' not found.")

    @property
    def name(self):
        return self.__name

    @property
    def elapsed_time(self):
        return self.__elapsed_time

    @property
    def mjd(self):
        return self.__mjd

    @property
    def values(self):
        return self.__series

    @property
    def duration(self):
        return (self.mjd[-1] - self.mjd[0]) * 86400

    def plot(self, **kwargs):
        show = kwargs.pop('show', True)
        self.__plot(show, kwargs)

    # def scatter(self, **kwargs):
    #     # TODO: Does not work with 2D value arrays
    #     show = kwargs.pop('show', True)
    #     self.__plot(plt.scatter, show, kwargs)

    def __plot(self, show, kwargs):
        if not PLOTTING_ENABLED:
            raise ValueError('Plotting is disabled because matplotlib could not be imported.')
        if self.__has_subseries:
            raise ValueError('Select a specific subseries to plot.')
        try:
            plt.plot(self.__elapsed_time, self.__series, **kwargs)
            plt.xlabel('Elapsed Time (s)')
            if show:
                plt.show()
        except Exception:
            raise ValueError("The data type of this series does not support plotting.")

    def to_file(self, filename):
        '''Save series to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'name': self.__name, 'time': self.__mjd, 'series': self.__series}
            json.dump(contents, json_file)
            print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename):
        '''Load series from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['name'], contents['time'], contents['series'])

    def summarize(self):
        hfill()
        print("Sedaro Simulation Series Summary".center(HFILL))
        print(f"'{self.name}'".center(HFILL))
        hfill()
        average_step = self.duration / len(self.elapsed_time)
        print(f"📈 {len(self.mjd)} points covering {self.duration/60:.1f} minutes with ~{average_step:.1f}s steps")

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
            print("❓ Call .<SUBSERIES_NAME> to select a subseries")
        else:
            print("❓ Call .plot to visualize results")
