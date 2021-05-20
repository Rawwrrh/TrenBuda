import json


class Data:
    @staticmethod
    def load(filename):
        filename = filename or "./metro.json"
        with open(filename, "r") as f:
            return json.loads(f.read())

    @staticmethod
    def parse(tree, Metro, Station):
        metro = Metro()
        metro.first = tree["first"]
        metro.last = tree["last"]

        stations = tree["stations"]

        # Create each station object
        for key in stations.keys():
            data = stations[key]
            id = data["id"]
            label = data["label"]
            station = Station(
                metro, id, label, data["color"], data["parents"], data["children"]
            )

            metro.stations[id] = station
            metro.labels[label] = station

        # Resolve references
        for station in metro.stations.values():
            station.load()

        return metro
