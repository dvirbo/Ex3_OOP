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
        g1 = DiGraph()
        pos = (4.9, 5.6, 6.3)
        for n in range(5):
            g1.add_node(n, pos)
        g1.add_edge(1, 2, 5.5)
        self.assertEqual(g1.e_size(), 1)

    def test_get_all_v(self):
        g1 = DiGraph()
        pos = (4.9, 5.6, 6.3)
        for n in range(5):
            g1.add_node(n, pos)

    def test_get_mc(self):
        g1 = DiGraph()
        pos = (4.9, 5.6, 6.3)
        for n in range(5):
            g1.add_node(n, pos)
        self.assertEqual(g1.get_mc(), 5)

    def test_add_node(self):
        g1 = DiGraph()
        pos = (4.9, 5.6, 6.3)
        self.assertTrue(g1.add_node(1, pos))

    def test_remove_node(self):
        g1 = DiGraph()
        pos = (4.9, 5.6, 6.3)
        for n in range(3):
            g1.add_node(n, pos)
        g1.remove_node(1)
        self.assertEqual(g1.v_size(), 2)

    def test_remove_edge(self):
        g1 = DiGraph()
        pos = (4.9, 5.6, 6.3)
        for n in range(3):
            g1.add_node(n, pos)
        g1.add_edge(0, 1, 1.1)
        g1.add_edge(1, 2, 1.1)
        self.assertEqual(g1.e_size(), 2)
        g1.remove_edge(1, 2)
        self.assertEqual(g1.e_size(), 1)


if __name__ == '__main__':
    unittest.main()