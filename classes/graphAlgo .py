import json
from typing import List

from Interfaces.GraphAlgoInterface import GraphAlgoInterface
from Interfaces.GraphInterface import GraphInterface
from classes.diGraph import DiGraph
from classes.position import Position


class GraphAlgo(GraphAlgoInterface):
    """
    this class represents directed weighted graph that include some algorithms
    """

    def __init__(self, graph: DiGraph = None):
        """
        this method inits the graph -> creates a new graph
       :param graph: the new graph
       """
        self.graph = DiGraph
        if graph is not None:
            self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the graph that the algo work on
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
         Loads a graph from a json file.
        :param file_name: The path to the json file
        :return True if the loading was successful, False o.w.
        """
        flag = True
        try:
            with open(file_name) as f:
                data = json.load(f)
            for node in data["Nodes"]:
                tmpPos = node["pos"]
                p = str(tmpPos)
                p = tuple(p.split(","))
                pos = Position(p)
                self.graph.add_node(node['id'], pos)
            for edges in data["Edges"]:
                self.graph.add_edge(edges["src"], edges["dest"], edges["w"])

        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        :param file_name: The path to the out file
        :return: True if the save was successful, False o.w.
        """
        flag = True
        data = {"Edges": [], "Nodes": []}
        try:
            for fKey in self.graph.get_all_v().keys():
                pos = str(self.graph.getNode(fKey).pos)
                if pos is not None:
                    data["Nodes"].append({"pos": pos, "id": fKey})
                else:
                    data["Nodes"].append({"id": fKey})
            for sKey in self.graph.all_out_edges_of_node(fKey):
                weight = self.graph.all_out_edges_of_node(fKey).get(sKey)
                data["Edges"].append({"src": fKey, "w": weight, "dest": sKey})
            finData = data.__str__()
            finData.replace(" ", "")
            finData.replace("'", "\"")
            with open(file_name, "w") as f:
                f.write(finData)
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

# if __name__ == '__main__':
# g1 = GraphAlgo()
# g1.load_from_json("data/A0.json")
