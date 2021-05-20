from .color import Color


class Direction:
    up = 0
    down = 1
    same = 2
    impossible = 3
    direction = None

    def __init__(self, train):

        self.direction = self.impossible

        # Travel through parents
        if train._origin.id > train._to.id:
            self.direction = self.up
            if train._to.isLast:
                self.direction = self.down

        # Travel through children
        if train._origin.id < train._to.id:
            self.direction = self.down
            if train._to.isFirst:
                self.direction = self.up

        # Root only have children
        if train._origin.isRoot:
            self.direction = self.down

        # Leaf only have parents
        if train._origin.isLeaf:
            self.direction = self.up

        # Check if there is no need to travel
        if train._origin.id == train._to.id:
            self.direction = self.same

        # Check if the train could reach the destination
        if train._color != Color.blank:
            if (
                train._origin.color != Color.blank
                and train._origin.color != train._color
                or train._to.color != Color.blank
                and train._to.color != train._color
            ):
                self.direction = self.impossible

    def isUp(self):
        return self.direction == self.up

    def isDown(self):
        return self.direction == self.down

    def isSame(self):
        return self.direction == self.same

    def isImpossible(self):
        return self.direction == self.impossible

    def __repr__(self):
        return str(self.direction)
