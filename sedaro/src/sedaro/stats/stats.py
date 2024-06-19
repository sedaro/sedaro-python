import json

class SimulationStats:
    def __init__(self, stats):
        self.__stats = stats

    def agent(self, id_or_name: str):
        NotImplemented

    def summarize(self):
        NotImplemented

    def get_all(self):
        return self.__stats

    def save(self, path: str):
        with open(path, 'w') as f:
            json.dump(self.get_all(), f)

    @classmethod
    def load(cls, path: str):
        with open(path, 'r') as f:
            return cls(json.load(f))


class AgentStats:
    def __init__(self, agent_name, stats):
        self.__agent_name = agent_name
        self.__stats = stats

    @property
    def name(self):
        return self.__agent_name

    def block(self, block_name):
        return BlockStats(block_name, self.__stats[block_name])

    def summarize(self):
        NotImplemented

    def get_all(self):
        return self.__stats

    def save(self, path: str):
        with open(path, 'w') as f:
            json.dump({'name': self.__agent_name, 'stats': self.get_all()}, f)

    @classmethod
    def load(cls, path: str):
        with open(path, 'r') as f:
            data = json.load(f)
            return cls(data['name'], data['stats'])


class BlockStats:
    def __init__(self, block_name, stats):
        self.__block_name = block_name
        self.__stats = stats

    @property
    def name(self):
        return self.__block_name

    def series(self, series_name):
        return SeriesStats(series_name, self.__stats[series_name])

    def summarize(self):
        NotImplemented

    def get_all(self):
        return self.__stats

    def save(self, path: str):
        with open(path, 'w') as f:
            json.dump({'name': self.__block_name, 'stats': self.get_all()}, f)

    @classmethod
    def load(cls, path: str):
        with open(path, 'r') as f:
            data = json.load(f)
            return cls(data['name'], data['stats'])


class SeriesStats:
    def __init__(self, series_name, stats):
        self.__series_name = series_name
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
        return self.__series_name

    def get_all(self):
        return self.__stats

    def save(self, path: str):
        with open(path, 'w') as f:
            json.dump({'name': self.__series_name, 'stats': self.get_all()}, f)

    @classmethod
    def load(cls, path: str):
        with open(path, 'r') as f:
            data = json.load(f)
            return cls(data['name'], data['stats'])