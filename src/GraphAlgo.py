import json

from src.Edge import Edge
from src.Graph import Graph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Node import Node


class GraphAlgo(GraphAlgoInterface):
    graph = None

    def __init__(self):
        self.graph = GraphInterface()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as f:
                new_Nodes = {}
                new_Edges = {}
                my_dict = json.load(f)
                list_Nodes = my_dict["Nodes"]
                list_Edges = my_dict["Edges"]
                for v in list_Nodes:
                    node = Node(id_num=v["id"], position=v["pos"])
                    new_Nodes[node.id] = node

                for i in list_Edges:
                    edge = Edge(src=i["src"], dest=i["dest"], weight=i["w"])
                    temp_dic = {edge.dest: edge.weight}
                    new_Edges[edge.src] = temp_dic
                new_graph = Graph(new_Nodes, new_Edges)
                self.graph = new_graph
                return True
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as outfile:
                json.dump(self.graph, outfile)
            return True
        except IOError as e:
            print(e)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            return float('inf'), []

        distances = {id1: 0.0}


        """
            Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            @param id1: The start node id
            @param id2: The end node id
            @return: The distance of the path, a list of the nodes ids that the path goes through
            Example:
    #      >>> from GraphAlgo import GraphAlgo
    #       >>> g_algo = GraphAlgo()
    #        >>> g_algo.addNode(0)
    #        >>> g_algo.addNode(1)
    #        >>> g_algo.addNode(2)
    #        >>> g_algo.addEdge(0,1,1)
    #        >>> g_algo.addEdge(1,2,4)
    #        >>> g_algo.shortestPath(0,1)
    #        (1, [0, 1])
    #        >>> g_algo.shortestPath(0,2)
    #        (5, [0, 1, 2])
            Notes:
            If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
            More info:
            https://en.wikipedia.org/wiki/Dijkstra's_algorithm
            """
        raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
            Finds the shortest path that visits all the nodes in the list
            :param node_lst: A list of nodes id's
            :return: A list of the nodes id's in the path, and the overall distance
            """

    def centerPoint(self) -> (int, float):
        """
            Finds the node that has the shortest distance to it's farthest node.
            :return: The nodes id, min-maximum distance
            """

    def plot_graph(self) -> None:
        """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None
            """
        raise NotImplementedError


if __name__ == '__main__':
    g = GraphAlgo()
    g.load_from_json("C:/Users/yuval/PycharmProjects/Ex3_OOP/src/data/A5_edited")
    print(g.graph.e_size())
