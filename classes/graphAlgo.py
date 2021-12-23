import json
import matplotlib.pyplot as plt
from typing import List

from numpy import random

from Interfaces.GraphAlgoInterface import GraphAlgoInterface
from Interfaces.GraphInterface import GraphInterface
from classes.diGraph import DiGraph
from classes.position import Position

min_x = min_y = max_x = max_y = 0


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
        """
         Loads a graph from a json file.
        :param file_name: The path to the json file
        :return True if the loading was successful, False o.w.
        """
        flag = True
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
            for node in data["Nodes"]:
                jpos = tuple(map(float, str(node["pos"]).split(",")))
                self.graph.add_node(node_id=node["id"], pos=jpos)
            for edge in data["Edges"]:
                self.graph.add_edge(id1=edge["src"], id2=edge["dest"], weight=edge["w"])

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
                    pos = str(pos)
                    pos = pos.replace("\'", "")
                    data["Nodes"].append({"pos": pos, "id": fKey})
                else:
                    data["Nodes"].append({"id": fKey})
                for sKey in self.graph.all_out_edges_of_node(fKey):
                    weight = self.graph.all_out_edges_of_node(fKey).get(sKey)
                    data["Edges"].append({"src": fKey, "w": weight, "dest": sKey})
                finData = data.__str__()
                finData = finData.replace(" ", "")
                finData = finData.replace("'", "\"")
                finData = finData.replace("(", "")
                finData = finData.replace(")", "")
                with open(file_name, "w") as outfile:
                    outfile.write(finData)
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

        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        :return: None
        """

        g = self.get_graph()
        plt.xlabel("X")
        plt.ylabel("-<")
        for src, node in g.get_all_v().items():
            if node.pos is None:  # call a func that generate the node rand pos
                p = self.randPos()
                node.pos = Position(p)
            plt.plot(node.pos.x, node.pos.y, marker='o', color='yellow', markerfacecolor='b', markersize=3)
            plt.text(node.pos.x, node.pos.y, str(node.key))

            for dest in g.all_out_edges_of_node(src).keys():
                x1 = g.get_all_v()[src].pos.x
                y1 = g.get_all_v()[src].pos.y
                if g.get_all_v()[dest].pos is None:
                    p = self.randPos()
                    g.get_all_v()[dest].pos = Position(p)
                x2 = g.get_all_v()[dest].pos.x
                y2 = g.get_all_v()[dest].pos.y
                plt.arrow(x1, y1, x2 - x1, y2 - y1, width=0.00001, linewidth=0.05)
        plt.title("Graph:" + g.__str__())
        plt.legend()
        plt.show()  # make graphics appear.

    def randPos(self):
        """
        this function generate random position for nods without position
        """
        self.min_max()
        if min_x == min_y == max_x == max_y == 0:  # didn't change:
            x = random.uniform(32, 33)
            y = random.uniform(35, 36)
            z = 0
            ans = x, y, z
            return ans
        count = 0
        for node in self.graph.get_all_v().values():
            if node.pos is not None:
                count += 1
        x = random.uniform(max_x, min_x)
        y = random.uniform(max_y, min_y)
        z = 0
        if count == 0:  # if all the nodes without pos:
            x = random.uniform(32, 33)
            y = random.uniform(35, 36)
            z = 0
            ans = x, y, z
        else:
            ans = x, y, z
        return ans

    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """

    def min_max(self):
        global min_x, min_y, max_x, max_y
        min_x = min(list(self.get_graph().get_all_v().values()), key=lambda n: n.pos[0]).pos[0]
        min_y = min(list(self.get_graph().get_all_v().values()), key=lambda n: n.pos[1]).pos[1]
        max_x = max(list(self.get_graph().get_all_v().values()), key=lambda n: n.pos[0]).pos[0]
        max_y = max(list(self.get_graph().get_all_v().values()), key=lambda n: n.pos[1]).pos[1]

    def __str__(self) -> str:
        return "\n|V|={} , |E|={}".format(len(self.get_graph().get_all_v()), self.graph.edgeCount)

    def __repr__(self) -> str:
        return self.graph.__repr__()


if __name__ == '__main__':
    g1 = DiGraph()
