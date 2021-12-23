import json
import sys
from typing import List

from src.DiGraph import DiGraph
from src.Edge import Edge
from src.Interfaces.GraphAlgoInterface import GraphAlgoInterface
from src.Interfaces.GraphInterface import GraphInterface
from src.Node import Node


class GraphAlgo(GraphAlgoInterface):
    graph = None
    distances = None

    def __init__(self):
        self.graph = GraphInterface()

        # distances = {id1, {id2, [float ,List]}}
        self.distances = {}

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
                 Loads a graph from a json file.
                :param file_name: The path to the json file
                :return True if the loading was successful, False o.w.
                """
        flag = True
        try:
            with open(file_name, "r") as f:
                new_Nodes = {}
                counter = 0
                my_dict = json.load(f)
                list_Nodes = my_dict["Nodes"]
                list_Edges = my_dict["Edges"]
                for v in list_Nodes:
                    position = v["pos"]
                    id_num = v["id"]
                    node = Node(id_num, position)
                    new_Nodes[node.key] = node

                for i in list_Edges:
                    edge = Edge(src=i["src"], dest=i["dest"], weight=i["w"])
                    new_Nodes[edge.src].add_out_edge(edge.dest, edge.weight)
                    new_Nodes[edge.dest].add_in_edge(edge.src, edge.weight)
                    counter += 1

                new_graph = DiGraph()
                new_graph.set_graph(new_Nodes, counter)
                self.graph = new_graph
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
            nodes = self.graph.get_all_v()
            for fKey in nodes.keys():
                pos = str(nodes.get(fKey).pos)
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
        """

        :param id1: src node
        :param id2: dest node
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if id1 == id2:
            return float('inf'), []

        # checking if self.distance has the answer
        if self.distances is not None \
                and self.distances.get(id1) is not None \
                and self.distances.get(id1).get(id2) is not None \
                and self.distances.get(id1).get(id2)[0] is not None \
                and self.distances.get(id1).get(id2)[0] != sys.float_info.max \
                and self.distances.get(id1).get(id2)[1] is not None:
            return self.distances.get(id1).get(id2)

        # src_distances a dict of id1 distances and path to the graph's nodes
        src_distances = {}
        src_distances[id1] = [0, None]
        nodes = self.graph.get_all_v()
        for i in nodes:
            current_key = i
            nodes.get(i).set_tag(0)

            # id1 is already define in src_distances (line 115)
            if current_key != id1:
                if self.distances is not None \
                        and self.distances.get(id1) is not None \
                        and self.distances.get(id1).get(current_key) is not None:
                    src_distances[current_key] = self.distances.get(id1).get(current_key)

                # if there's an edge between src and dest then put the weight of the edge
                elif nodes.get(id1).get_edge(current_key) is not None:
                    temp_path = [id1, current_key]
                    src_distances[current_key] = [nodes.get(id1).get_edge(current_key).weight, temp_path]
                else:
                    src_distances[current_key] = [sys.float_info.max, None]

        while nodes.get(id2).tag != 1:
            # getting the node with the lowest distance from id1
            index = self.lowest_dist(src_distances, nodes)
            if index == -1:
                return src_distances[id2]
            else:
                self.Dijkstra_algorithm_path(index, src_distances)
                nodes.get(index).set_tag(1)

        self.distances[id1] = src_distances

        return src_distances[id2]

    def lowest_dist(self, src_distances: dict, nodes: dict) -> int:
        """

        :param nodes: dictionary of the graph's nodes
        :param src_distances: dictionary with the src distances to the other nodes in the graph
        :return: the index of the node with the lowest distance to src node
        """
        answer = sys.float_info.max
        index = -1

        for i in src_distances:
            key = i
            value = src_distances[key][0]

            current_node = nodes.get(key)
            if current_node.tag == 0:
                if value < answer:
                    answer = value
                    index = key
        return index

    def Dijkstra_algorithm_path(self, index: int, src_distances: dict) -> None:
        """

        :param index: current node to check
        :param src_distances: src_distances: dictionary with the src distances to the other nodes in the graph
        :return: void, updating src_distances if theres a new lower distance
        """
        dist = src_distances[index][0]
        edges = self.graph.all_out_edges_of_node(index)

        for edge in edges:
            dest_node = edges[edge].dest
            new_dist = dist + edges[edge].weight

            if new_dist < src_distances[dest_node][0]:
                temp_list = src_distances[index][1]

                src_distances[dest_node] = [new_dist, [x for x in temp_list]]
                src_distances[dest_node][1].append(dest_node)

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

        node_size = self.graph.v_size()
        if node_size == 0:
            return None
        if node_size == 1:
            return self.graph.get_all_v().keys(), None

        min_value = sys.float_info.max
        answer = 0

        for i in self.graph.get_all_v():
            current_key = i

            temp_max = 0
            max_value = sys.float_info.min

            for j in self.graph.get_all_v():
                next_node = j
                # checking if self.distances has the value
                if self.distances is not None \
                        and self.distances.get(current_key) is not None \
                        and self.distances.get(current_key).get(next_node) is not None \
                        and self.distances.get(current_key).get(next_node)[0] is not None \
                        and self.distances.get(current_key).get(next_node)[0] != sys.float_info.max:
                    temp_max = self.distances.get(current_key).get(next_node)[0]
                elif current_key != next_node:
                    temp_short = self.shortest_path(current_key, next_node)
                    temp_max = temp_short[0]

                # getting the max value of the current node distances
                if temp_max > max_value:
                    max_value = temp_max
            if max_value < min_value:
                min_value = max_value
                answer = current_key

        return answer, min_value

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
    g.load_from_json("C:/Users/yuval/PycharmProjects/Ex3_OOP/data/A0.json")
    print(g.shortest_path(0, 1))
    print(g.centerPoint())
