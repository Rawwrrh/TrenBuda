from .color import Color
from .direction import Direction
from .travel import Travel


class Train:
    _metro = None
    _color = None
    _origin = None
    _to = None
    _travel = None
    shortest = None

    def __init__(self):
        self._metro = None
        self._color = None
        self._origin = None
        self._to = None
        self._travel = None

    @staticmethod
    def new(metro):
        return Train().metro(metro)

    @staticmethod
    def red(metro):
        return Train.new(metro).color(Color.red)

    @staticmethod
    def green(metro):
        return Train.new(metro).color(Color.green)

    def metro(self, metro):
        self._metro = metro
        return self

    def color(self, color):
        if color:
            self._color = color.lower()

        Color.check(self._color)
        return self

    def origin(self, id):
        self._origin = self._metro.station(id)
        return self

    def to(self, id):
        self._to = self._metro.station(id)
        return self

    def travel(self):
        direction = Direction(self)
        if direction.isSame():
            raise Exception(f"You are already in station {self._origin}")

        if direction.isImpossible():
            raise Exception(
                f"The train is {self._color}. Is impossible to go from {self._origin} to {self._to}"
            )

        self._travel = Travel(self, direction).go()
        self.shortest = self._travel.shortest

        return self

    def __repr__(self):
        return f"Train > color: {self._color} | from: {self._origin} | to: {self._to} | shortest: {self._travel.shortest}"
