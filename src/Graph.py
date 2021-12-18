from src.Edge import Edge
from src.GraphInterface import GraphInterface
from src.Node import Node


class Graph(GraphInterface):
    nodes = None
    edges = None
    mc = None

    def __init__(self, nodes: dict, edges: dict):
        self.nodes = nodes
        self.edges = edges
        self.mc = 0

    def v_size(self):
        try:
            return len(self.nodes)
        except NotImplementedError as e:
            print(e)

    def e_size(self) -> int:
        try:
            return len(self.edges)
        except NotImplementedError as e:
            print(e)

    def get_all_v(self) -> dict:
        try:
            return self.nodes
        except NotImplementedError as e:
            print(e)

    def all_in_edges_of_node(self, id1: int) -> dict:
        try:
            ans = {}
            for i in self.edges:
                if self.edges.get(i).dest == id1:
                    ans[i] = self.nodes.get(i)
            return ans
        except NotImplementedError as e:
            print(e)

    def all_out_edges_of_node(self, id1: int) -> dict:
        try:
            return self.edges.get(id1)
        except NotImplementedError as e:
            print(e)

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
                new_edge = Edge(id1, id2, weight)
                self.edges[id1] = {id2: new_edge}
                self.mc += 1
                return True
            else:
                if self.edges.get(id1).get(id2).weight > weight:
                    del self.edges.get(id1)[id2]
                    new_edge = Edge(id1, id2, weight)
                    self.edges[id1] = {id2: new_edge}
                    self.mc += 1
                    return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id) is None:
            self.nodes[node_id] = Node(node_id, pos)
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        try:
            if self.nodes.get(node_id) is not None:
                del self.nodes[node_id]
                self.mc += 1
            return True
        except NotImplementedError as e:
            print(e)
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        try:
            if self.edges.get(node_id1).get(node_id2) is not None:
                del self.edges.get(node_id1)[node_id2]
                self.mc += 1
            return True
        except NotImplementedError as e:
            print(e)
        return False
