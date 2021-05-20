class Station:
    id = 0
    label = ""
    color = None
    parents = []
    children = []
    metro = None

    isRoot = False
    isLeaf = False
    isFirst = False
    isLast = False

    def __init__(self, metro, id, label, color, parents, children):
        self.metro = metro
        self.id = id
        self.label = label
        self.color = color

        self.parent_ids = parents or []
        self.children_ids = children or []

        self.parents = []
        self.children = []

        self.isFirst = False
        self.isLast = False
        self.isRoot = False
        self.isLeaf = False

        if id == metro.first:
            self.isFirst = True

        if id == metro.last:
            self.isLast = True

        if not parents or len(parents) < 1:
            self.isRoot = True

        if not children or len(children) < 1:
            self.isLeaf = True

    def load(self):
        for pid in self.parent_ids:
            self.parents.append(self.metro.station(pid))

        for cid in self.children_ids:
            self.children.append(self.metro.station(cid))

    def __repr__(self):
        return f"{self.label} (color: {self.color})"
