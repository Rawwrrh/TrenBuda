from .color import Color


class Travel:
    train = None
    direction = None
    paths = []
    shortest = None

    def __init__(self, train, direction):
        self.train = train
        self.direction = direction
        self.paths = []
        self.shortest = None

    def next(self, origin):
        if self.direction.isDown():
            return origin.children
        return origin.parents

    def go(self):

        self.paths = []

        # Get all the possible paths
        # using Breadth-first search (BFS)
        # see https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/

        explored = []
        queue = [[self.train._origin]]

        while queue:
            path = queue.pop(0)
            station = path[-1]

            if station not in explored:
                neighbours = self.next(station)
                for neighbour in neighbours:
                    newpath = list(path)
                    newpath.append(neighbour)
                    queue.append(newpath)

                    if neighbour.id == self.train._to.id:
                        # Found the path to the station
                        self.paths.append(newpath)

                explored.append(station)

        # Now we filter out the stations by colors
        paths = []
        for candidate in self.paths:
            stations = []
            for station in candidate:
                if self.train._color != Color.blank:
                    if station.color != Color.blank:
                        if station.color == self.train._color:
                            stations.append(station)
                    else:
                        stations.append(station)
                else:
                    stations.append(station)
            paths.append(stations)

        # And order by the number of stations
        # The first option should be the shortest path
        self.paths = sorted(paths, key=len, reverse=False)
        if len(self.paths) > 0:
            self.shortest = self.paths[0]

        return self

    def __repr__(self):
        return f"paths: {self.paths} | shortest: {self.shortest} (length: {len(self.shortest)})"
