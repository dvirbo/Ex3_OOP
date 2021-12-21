import json
import sys
from typing import List

from src.Edge import Edge
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
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
        try:
            with open(file_name, "r") as f:
                new_Nodes = {}
                my_dict = json.load(f)
                list_Nodes = my_dict["Nodes"]
                list_Edges = my_dict["Edges"]
                counter = 0
                for v in list_Nodes:
                    node = Node(id_num=v["id"], position=v["pos"])
                    new_Nodes[node.id] = node

                for i in list_Edges:
                    edge = Edge(src=i["src"], dest=i["dest"], weight=i["w"])
                    new_Nodes[edge.src].outEdges[edge.dest] = edge
                    new_Nodes[edge.dest].inEdges[edge.src] = edge
                    counter += 1
                new_graph = DiGraph(new_Nodes)
                new_graph.edgeCount = counter
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
        """

        :param id1: src node
        :param id2: dest node
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if id1 == id2:
            return float('inf'), []

        if self.distances is not None \
                and self.distances.get(id1) is not None \
                and self.distances.get(id1).get(id2) is not None \
                and self.distances.get(id1).get(id2)[0] is not None \
                and self.distances.get(id1).get(id2)[0] != sys.float_info.max \
                and self.distances.get(id1).get(id2)[1] is not None:
            return self.distances.get(id1).get(id2)

        diGraph = DiGraph(self.graph.get_all_v())

        src_distances = {}
        src_distances[id1] = [0, None]
        for i in self.graph.get_all_v():
            current_key = i
            diGraph.getNode(i).set_tag(0)

            if current_key != id1:
                if self.distances is not None \
                        and self.distances.get(id1) is not None \
                        and self.distances.get(id1).get(current_key) is not None:
                    src_distances[current_key] = self.distances.get(id1).get(current_key)

                # if there's an edge between src and dest then put the weight of the edge
                elif diGraph.get_edge(id1, current_key) is not None:
                    temp_path = [id1, current_key]
                    src_distances[current_key] = [diGraph.get_edge(id1, current_key).weight, temp_path]
                else:
                    src_distances[current_key] = [sys.float_info.max, None]

        while diGraph.getNode(id2).tag != 1:
            # getting the node with the lowest distance from id1
            index = self.lowest_dist(src_distances, diGraph)
            if index == -1:
                return src_distances[id2]
            else:
                self.Dijkstra_algorithm_path(index, src_distances, diGraph)
                diGraph.getNode(index).set_tag(1)

        self.distances[id1] = src_distances

        return src_distances[id2]

    def lowest_dist(self, src_distances: dict, diGraph: DiGraph) -> int:
        """

        :param src_distances: dictionary with the src distances to the other nodes in the graph
        :param diGraph: this graph
        :return: the index of the node with the lowest distance to src node
        """
        answer = sys.float_info.max
        index = -1

        for i in src_distances:
            key = i
            value = src_distances[key][0]

            current_node = diGraph.getNode(key)
            current_tag = current_node.tag
            if current_tag == 0:
                if value < answer:
                    answer = value
                    index = key
        return index

    def Dijkstra_algorithm_path(self, index: int, src_distances: dict, diGraph: DiGraph) -> None:
        """

        :param index: current node to check
        :param src_distances: src_distances: dictionary with the src distances to the other nodes in the graph
        :param diGraph: this graph
        :return: void, updating src_distances if theres a new lower distance
        """
        dist = src_distances[index][0]
        edges = diGraph.all_out_edges_of_node(index)

        for edge in edges:
            dest_node = edges[edge].dest
            new_dist = dist + edges[edge].weight

            if new_dist < src_distances[dest_node][0]:
                src_distances[dest_node] = [new_dist, None]
                src_distances.get(dest_node)[1] = src_distances.get(index)[1]
                src_distances.get(dest_node)[1].append(dest_node)
                src_distances.get(index)[1].remove(dest_node)

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

        if self.graph.v_size() == 0:
            return None
        if self.graph.v_size() == 1:
            return self.graph.get_all_v()

        min_value = sys.float_info.max
        answer = 0

        for i in self.graph.get_all_v():
            current_key = i

            temp_max = 0
            max_value = sys.float_info.min

            for j in self.graph.get_all_v():
                next_node = j

                if self.distances is not None \
                        and self.distances.get(current_key) is not None \
                        and self.distances.get(current_key).get(next_node) is not None \
                        and self.distances.get(current_key).get(next_node)[0] is not None \
                        and self.distances.get(current_key).get(next_node)[0] != sys.float_info.max:
                    temp_max = self.distances.get(current_key).get(next_node)[0]
                elif current_key != next_node:
                    temp_short = self.shortest_path(current_key, next_node)
                    temp_max = temp_short[0]

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
    print(g.graph.e_size())
    print(g.shortest_path(0, 1))
    print(g.centerPoint())
