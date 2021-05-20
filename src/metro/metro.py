from .data import Data
from .station import Station


class Metro:
    first = 0
    last = 0

    # Get station by id
    stations = {}

    # Get station by label
    labels = {}

    def __init__(self):
        self.first = 0
        self.last = 0
        self.stations = {}
        self.labels = {}

    def station(self, id):
        exception = Exception(f"Station identified by '{id}' was not found.")
        try:
            id = int(id)
        except Exception:
            if id not in self.labels.keys():
                raise exception
            return self.labels[id]

        if id not in self.stations.keys():
            raise exception
        return self.stations[id]

    @staticmethod
    def fromJson(filename=None):
        tree = Data.load(filename)
        metro = Data.parse(tree, Metro, Station)
        return metro

    def __repr__(self):
        return f"first: {self.first}, last: {self.last}, stations: {self.stations}"
