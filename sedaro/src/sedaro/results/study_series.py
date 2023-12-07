import gzip
import json
from functools import cached_property

from scipy.interpolate import interp1d

try:
    import matplotlib.pyplot as plt
except ImportError:
    PLOTTING_ENABLED = False
else:
    PLOTTING_ENABLED = True


from .utils import HFILL, _get_series_type, bsearch, hfill



class StudySeries:

    def __init__(self, study_id, name,series):
        self._study_id = study_id
        self._name = name
        self._series = series
        self._first_sim_id, self._first_series = next(iter(series.items()))

    def __repr__(self):
        return f"Study Series({self._name})"

    def __iter__(self): 
        '''Iterate through study series.

        Only a series with no subseries is iterable.
        '''
        if self._first_series.has_subseries:
            raise ValueError('Select a specific subseries to iterate over.')
        return ( {sim_id:series} for (sim_id, series) in self._series.items())

    def __len__(self) -> int:
        return { sim_id: len(series.mjd) for (sim_id, series) in self._series.items() }

    def __getitem__(self, subseries_name: str):
        '''Get a particular subseries by name.

        Typically invoked by indexing [<SUBSERIES_NAME>] on an instance
        of SedaroSeries. Can only be called if the series has subseries.
        '''
        if not self._first_series.has_subseries:
            raise ValueError('This series has no subseries.')
        elif subseries_name in self._first_series._SedaroSeries__series:
            new_series_name = f'{self._name}.{subseries_name}'

            sub_subseries = { sim_id: series[subseries_name] for (sim_id,series) in self._series.items()}

            return StudySeries(self._study_id, new_series_name, sub_subseries)
        else:
            raise ValueError(f"Subseries '{subseries_name}' not found.")

    def __getattr__(self, subseries_name: str):
        '''Get a particular subseries by name as an attribute.'''
        return {sim_id: series[subseries_name] for (sim_id, series) in self._series.items()} 

    @property
    def has_subseries(self):
        return self._first_series.has_subseries

    @property
    def name(self):
        return self._name

    @property
    def elapsed_time(self):
        return  {sim_id: series.elapsed_time for (sim_id, series) in self._series.items()}  

    @property
    def mjd(self):
        return {sim_id: series.mjd for (sim_id, series) in self._series.items()}

    @property
    def values(self):
        return self._series

    @property
    def subtypes(self):
        if self._first_series.has_subseries:
            return self._first_series._SedaroSeries__dtype.items()
        else:
            return {}

    @cached_property
    def values_interpolant(self):
        return { sim_id: series.values_interpolant for (sim_id, series) in self._series.items() }

    @property
    def duration(self):
        return { sim_id: series.duration for (sim_id, series) in self._series.items()}

    def value_at(self, mjd, interpolate=False):
        '''Get the value of this series at a particular time in mjd.'''
        return { sim_id: series.value_at(mjd, interpolate) for (sim_id, series) in self._series.items()}

    def plot(self, show=True, ylabel=None, elapsed_time=True, height=None, xlim=None, ylim=None, **kwargs):
        self.__plot(show, ylabel, elapsed_time, height, xlim, ylim, **kwargs)

    def __plot(self, show, ylabel, elapsed_time, height, xlim, ylim, **kwargs):
        for (sim_id, series) in self._series.items():
            series.plot(False, ylabel, elapsed_time, height, xlim, ylim, label=sim_id, **kwargs)
        plt.legend()
        plt.title(f"Study:{self._study_id}:{self._name}")
        if show:
            plt.show()

    def sim_stats(self, job_id, output_html=False):
        if job_id in self._series:
            self._series[job_id].stats(output_html)
        else:
            print(f"Error: Study sim id {sim_id} not found.") 
            self._print_sim_ids()

    def to_file(self, filename, verbose=True):
        pass

    @classmethod
    def from_file(cls, filename):
        pass

    def _print_sim_ids(self):
        hfill()
        print(f"Study Simulation ID's".center(HFILL))
        print(f'\n {str( list(self._series.keys()) )}')
        hfill()

    def summarize(self):
        hfill()
        print(f"Study Simulation Series Result Summary".center(HFILL))
        print(f"'{self._name}'".center(HFILL))
        print(f"Study ID: '{self._study_id}'".center(HFILL))

        self._print_sim_ids()

        print("Study Simulation Series Data Summary".center(HFILL))
        print(f"'{self._name}'".center(HFILL))
        hfill()

        average_step = { sim_id: series.duration / len(series.elapsed_time) for (sim_id, series) in self._series.items() }

        for (sim_id, series) in self._series.items():
            print(f"📈 sim_id:{sim_id} {len(series)} points covering {series.duration/60:.1f} minutes with ~{average_step[sim_id]:.1f}s steps")

        if self._first_series.has_subseries:
            print("\n📑 This series has subseries.")
            print(f"\n🗂️ Value data types are:")
            for key, value in self._first_series._SedaroSeries__dtype.items():
                if value == 'None':
                    print(f"    - '{key}': All entries in this subseries are None")
                else:
                    print(f"    - '{key}': '{value}'")

        else:
            if self._first_series._SedaroSeries__dtype == 'None':
                print('\n⛔ All entries in this series are None')
            else:
                print(f"\n🗂️ Value data type is '{self._first_series._SedaroSeries__dtype}'")

        hfill()
        if self._first_series.has_subseries:
            print("❓ Index [<SUBSERIES_NAME>] to select a subseries")
        else:
            print("❓ Call .plot to visualize results of all study series results")
            print("📊 Display statistics with .sim_stats(sim_id, output_html=False ) ")



