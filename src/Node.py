class Node:

    id = None
    tag = 0
    weight = None
    inEdges = {}
    outEdges = {}
    pos = None

    def __init__(self, id_num: int, position: tuple):
        """
        :param id_num: uniq key of the node
        :param position: geo position
        """
        self.id = id_num
        self.tag = 0
        self.weight = None
        self.inEdges = {}
        self.outEdges = {}
        self.pos = position

    def get_key(self) -> int:
        return self.id

    def set_tag(self, tag):
        self.tag = tag

    def get_edge(self, id2: int):
        try:
            return self.outEdges[id2]
        except KeyError:
            return None

    def set_inEdges(self, new_inEdges: dict):
        self.inEdges = new_inEdges

    def set_outEdges(self, new_outEdges: dict):
        self.outEdges = new_outEdges

    def __str__(self) -> str:
        return f"id: {self.id}, pos: {self.pos}"

    def __repr__(self) -> str:
        return f"id: {self.id}, pos: {self.pos}"
