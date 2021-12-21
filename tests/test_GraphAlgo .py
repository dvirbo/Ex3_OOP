import unittest
import sys
from classes.node import Node
from classes.diGraph import DiGraph


class TestGraphAlgo(unittest.TestCase):

    def test_saveAndLoad_to_json(self):
        g1 = GraphAlgo()
        g1.load_from_json('data/A0.json')
        print(g1.graph.nodes.keys())

    def test_shortest_path(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
