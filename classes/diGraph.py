from classes.edge import Edge
from Interfaces.GraphInterface import GraphInterface
from node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.mcCount = 0
        self.edgeCount = 0

    def set_graph(self, new_node: dict, edge_count: int):
        self.nodes = new_node
        self.edgeCount = edge_count

    def v_size(self):
        try:
            return len(self.nodes)
        except NotImplementedError as e:
            print(e)

    def e_size(self) -> int:
        try:
            return self.edgeCount
        except NotImplementedError as e:
            print(e)

    def get_all_v(self) -> dict:
        try:
            return self.nodes
        except NotImplementedError as e:
            print(e)

    def set_all_v(self, nodes: dict):
        self.nodes = nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        try:
            return self.getNode(id1).inEdges
        except NotImplementedError as e:
            print(e)

    def all_out_edges_of_node(self, id1: int) -> dict:
        try:
            return self.getNode(id1).outEdges
        except NotImplementedError as e:
            print(e)

    def get_mc(self) -> int:
        return self.mcCount

    def __contains__(self, key):
        """
        this function check if the key part of the dict of the nodes
        :param key: the key of the uniq node
        :return: true of the dictionary of the nodes contain the key
        """
        return key in self.nodes

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        :param id1: The start node of the edge
        :param id2: The end node of the edge
        :param weight: The weight of the edge
        :return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 is not id2 and weight >= 0:
            if (self.__contains__(id1)) & (self.__contains__(id2)):  # check if there in the dict nodes
                if (id1 not in self.all_in_edges_of_node(id2).keys()) & (
                        id2 not in self.all_out_edges_of_node(id1).keys()):
                    self.nodes[id1].outEdges[id2] = Edge(id1, id2, weight)
                    self.nodes[id2].inEdges[id1] = Edge(id2, id1, weight)
                    self.mcCount += 1
                    self.edgeCount += 1
                    return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
                Adds a node to the graph.
                :param node_id: The node ID
                :param pos: The position of the node
                :return: True if the node was added successfully, False o.w.
                Note: if the node id already exists the node will not be added
                """
        if node_id in self.nodes.keys():  # if the node id already exists
            return False
        n = Node(node_id, pos)
        self.nodes[node_id] = n
        self.mcCount += 1
        return True

    def getNode(self, key: int):
        """
        :param key:  the key of the node that we want to
        :return the node
        KeyError - Raised when a mapping (dictionary) key is not found in the set of existing keys.
        """
        try:
            return self.nodes[key]
        except KeyError:
            return None

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        :param node_id: The node ID
        :return True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.nodes.keys():  # if the node id isn't exists in the dict of nodes
            return False
        for i in self.all_in_edges_of_node(node_id):
            del self.nodes[i].outEdges[node_id]
            self.edgeCount -= 1
        for i in self.all_out_edges_of_node(node_id):
            del self.nodes[i].inEdges[node_id]
            self.edgeCount -= 1
        del self.nodes[node_id]
        self.mcCount += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        :param node_id1: The start node of the edge
        :param node_id2: The end node of the edge
        :return True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if (node_id1 in self.all_in_edges_of_node(node_id2).keys()) & (
                node_id2 in self.all_out_edges_of_node(node_id1).keys()):
            del self.nodes[node_id1].outEdges[node_id2]
            del self.nodes[node_id2].inEdges[node_id1]
            self.mcCount += 1
            self.edgeCount -= 1
            return True
        return False

    def get_edge(self, id1: int, id2: int):
        try:
            return self.getNode(id1).get_edge(id2)
        except KeyError:
            return None

    def __str__(self):
        return "\n|V|={} , |E|={}".format(len(self.nodes), self.edgeCount)

    def __repr__(self) -> str:
        return self.__repr__()
