from typing import List

from Interfaces import GraphInterface
from Interfaces import GraphAlgoInterface
from classes import DiGraph


class GraphAlgo(GraphAlgoInterface):
    """
    this class represents directed weighted graph that include some algorithms
    """

    def __init__(self, graph: DiGraph = None):
        """
        this method inits the graph -> creates a new graph
       :param graph: the new graph
       """
        self.graph = DiGraph()
        if graph is not None:
            self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the graph that the algo work on
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass