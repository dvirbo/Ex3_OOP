from src.Edge import Edge
from src.Node import Node


class Graph:
    nodes = None
    edges = None
    mc = None

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def v_size(self):
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for i in self.edges:
            if self.edges.get(i).dest == id1:
                ans.update({i: self.nodes.get(i)})

        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes.get(id1) is None:
            raise NotImplementedError
        if self.nodes.get(id2) is None:
            raise NotImplementedError
        if weight < 0:
            raise
        if id1 != id2:
            if self.edges.get(id1).get(id2) is None:
                new_edge = Edge(id1, weight, id2)
                new_edge_dict = {id2: new_edge}
                self.edges.update({id1: new_edge_dict})
                return True
            else:
                if self.edges.get(id1).get(id2).weight > weight:
                    del self.edges.get(id1)[id2]
                    new_edge = Edge(id1, weight, id2)
                    new_edge_dict = {id2: new_edge}
                    self.edges.get(id1).update({id2: new_edge_dict})
                    return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id) is None:
            new_node = Node(node_id, pos)
            self.nodes.update({node_id: new_node})
            return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.get(node_id) is not None:
            del self.nodes[node_id]
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.edges.get(node_id1).get(node_id2) is not None:
            del self.edges.get(node_id1)[node_id2]
            return True
