import json
import sys
import matplotlib.pyplot as plt
from typing import List
from numpy import random

from src.diGraph import DiGraph
from src.edge import Edge
from src.Interfaces.GraphAlgoInterface import GraphAlgoInterface
from src.Interfaces.GraphInterface import GraphInterface
from src.node import Node
from src.position import Position

min_x = min_y = max_x = max_y = 0


class GraphAlgo(GraphAlgoInterface):
    graph = None
    distances = None
    connected = -1

    def _init_(self, directedGraph: DiGraph() = None) -> None:
        """
        this method inits the graph -> creates a new graph
       :param directedGraph: the new graph
       """
        # distances = {id1, {id2, [float ,List]}}
        self.distances = {}
        self.connected = -1

        self.graph = DiGraph()
        if directedGraph is not None:
            if isinstance(directedGraph, DiGraph):
                self.graph = directedGraph

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
                    if len(v) == 1:
                        position = None
                    else:
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
                self._init_(new_graph)
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
                    w = self.graph.all_out_edges_of_node(fKey).get(sKey)
                    w = str(w)
                    weight = w[-3:]
                    data["Edges"].append({"src": fKey, "w": weight, "dest": sKey})
                finData = data._str_()
                # finData = finData.replace(" ", "")
                finData = finData.replace("'", "\"")
                with open(file_name, "w") as f:
                    f.write(finData)
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
        for current_key in nodes:
            nodes.get(current_key).set_tag(0)

            # id1 is already define in src_distances (line 116)
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
                return float('inf'), []
            else:
                self.Dijkstra_algorithm_path(index, src_distances)
                nodes.get(index).set_tag(1)

        self.distances[id1] = src_distances
        return src_distances[id2]

    def lowest_dist(self, src_distances: dict, nodes: dict) -> int:
        """

        :param nodes: dictionary of the graph's nodes
        :param src_distances: dictionary with the src distances to the other nodes in the graph
        :return: The index of the node with the lowest distance from src node
        """
        temp_dist = sys.float_info.max
        ans = -1

        for i in src_distances:
            key = i
            value = src_distances[key][0]

            current_node = nodes.get(key)
            if current_node.tag == 0:
                if value < temp_dist:
                    temp_dist = value
                    ans = key
        return ans

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
        if not len(node_lst):
            pass

        #  removing duplicates
        node_lst = list(dict.fromkeys(node_lst))

        pathAns = []

        # path from nodeA to nodeB while nodeA is startNode and nodeB is the node with the lowest distance from nodeA
        tempPath = []
        cost = sys.float_info.max

        startNode = node_lst.pop(0)
        currentNode = 0
        pathAns.append(startNode)

        # dist_ans -> overall distance
        dist_ans = 0

        # while node_lst is not empty
        while node_lst:

            # looking for the node with the lowest distance path from startNode
            for next_node_key in node_lst:
                if self.distances is not None \
                        and self.distances.get(startNode) is not None \
                        and self.distances.get(startNode).get(next_node_key) is not None \
                        and self.distances.get(startNode).get(next_node_key)[0] is not None \
                        and self.distances.get(startNode).get(next_node_key)[0] != sys.float_info.max \
                        and self.distances.get(startNode).get(next_node_key)[1] is not None:
                    tempSPD = self.distances.get(startNode).get(next_node_key)[0]

                else:
                    tempSPD = self.shortest_path(startNode, next_node_key)[0]

                if tempSPD < cost:
                    cost = tempSPD
                    tempPath = self.distances.get(startNode).get(next_node_key)[1]
                    dist_ans += self.distances.get(startNode).get(next_node_key)[0]
                    tempPath.remove(startNode)
                    currentNode = next_node_key

            #  if there's no path
            if not tempPath:
                return -1, float('inf')

            cost = sys.float_info.max
            index = node_lst.index(currentNode)
            startNode = node_lst[index]

            for i in tempPath:
                pathAns.append(i)
                if i in node_lst:
                    node_lst.remove(i)

        return pathAns, dist_ans

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
        if self.connected == -1:
            if not self.is_connected:
                return -1, float('inf')
        elif self.connected == 0:
            return -1, float('inf')

        min_value = sys.float_info.max
        answer = 0

        for current_key in self.graph.get_all_v():
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

    def is_connected(self) -> bool:
        """

        :return: Returns True if and only if (iff) there is a valid path from each node to each other node.
        """
        edges = self.graph.e_size()
        nodes = self.graph.v_size()

        #  a connected graph with n vertex must have at list n-1 edges
        if edges < nodes - 1:
            self.connected = 0
            return False

        self.DFS(self.graph.get_all_v().get(0))

        for i in self.graph.get_all_v():
            node = self.graph.get_all_v().get(i)
            # if there's a node in the graph that DFS didn't reach to then the graph is not connected
            if node.tag == 0:
                self.connected = 0
                return False

        self.connected = 1
        return True

    def DFS(self, n: Node):
        """

        :param n: current node to check path to other nodes
        :return: void, setting node's tag to 1 when reached to
        """
        n.set_tag(1)

        for i in self.graph.all_out_edges_of_node(n.key):
            nd = self.graph.get_all_v().get(i)
            if nd.tag == 0:
                self.DFS(nd)

        n.set_tag(2)

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        :return: None
        """
        gp = self.get_graph()
        plt.xlabel("X")
        plt.ylabel("-<")
        for src, node in gp.get_all_v().items():
            if node.pos is None:
                x = random.uniform(0.0, 100)
                y = random.uniform(0.0, 100)
                p = (x, y, 0)
                node.pos = Position(p)
            plt.plot(node.pos.x, node.pos.y, marker='o', color='yellow', markerfacecolor='b', markersize=3)
            plt.text(node.pos.x, node.pos.y, str(node.key))

            for dest in gp.all_out_edges_of_node(src).keys():
                x1 = gp.get_all_v()[src].pos.x
                y1 = gp.get_all_v()[src].pos.y
                if gp.get_all_v()[dest].pos is None:
                    x = random.uniform(0.0, 100)
                    y = random.uniform(0.0, 100)
                    p = (x, y, 0)
                    gp.get_all_v()[dest].pos = Position(p)
                x2 = gp.get_all_v()[dest].pos.x
                y2 = gp.get_all_v()[dest].pos.y
                plt.arrow(x1, y1, x2 - x1, y2 - y1, width=0.00001, linewidth=0.05)
        plt.title("Graph:" + gp.__str__())
        # plt.legend()
        plt.show()  # make graphics appear.

    # def __str__(self) -> str:
    #     return "\n|V|={} , |E|={}".format(len(self.get_graph().get_all_v()), self.graph.edgeCount)
    #
    # def __repr__(self) -> str:
    #     return self.graph.__repr__()


if __name__ == '__main__':
    g = GraphAlgo()
    g.load_from_json("C:/Users/yuval/PycharmProjects/Ex3_OOP/data/A0.json")
    print(g.shortest_path(0, 1))
    print(g.centerPoint())
    listi = [1, 2, 3]
    print(g.is_connected)
    print(g.TSP(listi))
