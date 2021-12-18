class Node:

    id = None
    pos = None
    tag = None
    weight = None

    def __init__(self, id_num: int, pos: tuple):
        self.id = id_num
        self.pos = pos
        self.weight = None
        self.tag = 0

