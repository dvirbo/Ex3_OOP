import unittest
from unittest import TestCase
from classes.diGraph import DiGraph


class TestDiGraph(TestCase):
    def test_v_size(self):
        g = DiGraph()
        pos = (4.9, 5.6, 6.3)
        for n in range(5):
            g.add_node(n, pos)
        self.assertEqual(g.v_size(), 5)
        g.remove_node(1)
        self.assertEqual(g.v_size(), 4)

    def test_e_size(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)

        g.add_edge(1, 2, 1.3334)
        g.add_edge(2, 3, 1.33221)
        g.add_edge(3, 1, 4.3221)
        g.add_edge(4, 3, 2.1)

        self.assertEqual(g.e_size(), 4)
        g.remove_node(1)
        self.assertEqual(g.e_size(), 2)

    def test_get_all_v(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)

        g.add_edge(1, 2, 1.321)
        g.add_edge(3, 2, 1.234)

        self.assertEqual(g.all_in_edges_of_node(2).get(1).weight, 1.321)

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for n in range(5):
            g.add_node(n)

        g.add_edge(1, 2, 1.3334)
        g.add_edge(1, 3, 1.433)
        g.add_edge(2, 3, 1.33221)
        g.add_edge(3, 1, 4.3221)
        g.add_edge(4, 3, 2.1)

        self.assertEqual(g.all_out_edges_of_node(1).get(3).weight, 1.433)

    # def test_get_mc(self):
    #
    # def test_contains(self, key):
    #
    # def test_add_edge(self, id1: int, id2: int, weight: float):
    #
    # def test_add_node(self, node_id: int, pos: tuple = None):
    #
    # def test_getNode(self, key: int):
    #
    # def test_remove_node(self, node_id: int):
    #
    # def test_remove_edge(self, node_id1: int, node_id2: int):
    #
    # def test_get_edge(self, id1: int, id2: int):


if __name__ == '__main__':
    unittest.main()
