class Edge:
    src = None
    dest = None
    weight = None

    def __init__(self, src: int, weight: float, dest: int):
        self.src = src
        self.weight = weight
        self.dest = dest

