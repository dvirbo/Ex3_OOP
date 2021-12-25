import unittest
import sys


from classes.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_saveLoad_to_json(self):
        g1 = GraphAlgo()
        g1.get_graph().add_node(0, (1.4, 2.2, 0.0))
        g1.get_graph().add_node(1, (1.5, 2.1, 0.0))
        g1.get_graph().add_node(2, (2.7, 3.8, 0.0))
        g1.get_graph().add_node(3, (1.9, 3.5, 0.0))
        g1.get_graph().add_edge(0, 1, 5.2)
        g1.get_graph().add_edge(1, 2, 3.1)
        g1.get_graph().add_edge(1, 0, 2.9)
        g1.get_graph().add_edge(3, 1, 1.1)
        g1.get_graph().add_edge(1, 3, 3.6)
        check = g1.save_to_json("../data/save_test.json")
        self.assertTrue(check)
        g2 = GraphAlgo()
        check = g2.load_from_json("../data/save_test.json")
        self.assertTrue(check)
        #
        # def test_shortest_path(self):
        #     self.fail()
        #
        # def test_tsp(self):
        #     self.fail()
        #
        # def test_center_point(self):
        #     self.fail()


if __name__ == '__main__':
    unittest.main()
