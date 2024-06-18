class SimulationStats:
    pass

class AgentStats:
    pass

class BlockStats:
    pass

class SeriesStats:
    def __init__(self, series, stats):
        self.__series = series
        self.__stats = stats

    @property
    def max(self):
        return self.__stats.max

    @property
    def min(self):
        return self.__stats.min

    @property
    def negativeMax(self):
        return self.__stats.negativeMax

    @property
    def positiveMax(self):
        return self.__stats.positiveMax

    @property
    def integral(self):
        return self.__stats.integral

    @property
    def average(self):
        return self.__stats.average

    @property
    def absAvg(self):
        return self.__stats.absAvg

    @property
    def name(self):
        return self.__series

    def get_all(self):
        return self.__stats