from classes.edge import Edge
from classes.position import Position


class Node:

    def __init__(self, id_num: int, position: tuple):
        """
        :param id_num: uniq key of the node
        :param position: geo position
        """
        self.key = id_num
        self.tag = 0
        self.weight = None
        self.inEdges = {}
        self.outEdges = {}
        if position is not None:
            self.pos = Position(position)
        else:
            self.pos = position

    def get_key(self) -> int:
        return self.key

    def set_tag(self, tag):
        self.tag = tag

    def get_edge(self, id2: int):
        try:
            return self.outEdges[id2]
        except KeyError:
            return None

    def __contains__(self, key):
        """
        this function check if the key part of the dict of the nodes
        :param key: the key of the uniq node
        :return: true of the dictionary of the nodes contain the key
        """
        return key in self.outEdges

    def add_out_edge(self, id2: int, weight: float):
        if weight >= 0:
            if self.__contains__(id2):  # check if there in the dict nodes
                if self.get_edge(id2).weight > weight:
                    self.outEdges[id2].weight = weight
            else:
                self.outEdges[id2] = Edge(self.key, id2, weight)

    def add_in_edge(self, id1: int, weight: float):
        if weight >= 0:
            if id1 in self.inEdges:  # check if there in the dict nodes
                if self.inEdges[id1][2] > weight:
                    self.inEdges[id1][2] = weight
            else:
                self.inEdges[id1] = Edge(id1, self.key, weight)

    def set_inEdges(self, new_inEdges: dict):
        self.inEdges = new_inEdges

    def set_outEdges(self, new_outEdges: dict):
        self.outEdges = new_outEdges

    def __str__(self) -> str:
        return f"id: {self.key}, pos: {self.pos}"

    def __repr__(self) -> str:
        return f"id: {self.key}, pos: {self.pos}"