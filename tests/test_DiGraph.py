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

    # def test_e_size(self):
    #     self.fail()
    #
    # def test_get_all_v(self):
    #     self.fail()
    #
    # def test_all_in_edges_of_node(self):
    #     self.fail()
    #
    # def test_all_out_edges_of_node(self):
    #     self.fail()
    #
    # def test_get_mc(self):
    #     self.fail()
    #
    # def test_add_node(self):
    #     self.fail()
    #
    # def test_get_node(self):
    #     self.fail()
    #
    # def test_remove_node(self):
    #     self.fail()
    #
    # def test_remove_edge(self):
    #     self.fail()


if __name__ == '__main__':
    unittest.main()
