import unittest

from classes.graphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    # def test_get_graph(self):
    #
    # def test_load_from_json(self):
    #
    # def test_save_to_json(self):

    def test_shortest_path(self):
        g = GraphAlgo()
        for n in range(10):
            g.graph.add_node(n)

        g.graph.add_edge(0, 1, 1.4004465106761335)
        g.graph.add_edge(0, 10, 1.4620268165085584)
        g.graph.add_edge(1, 0, 1.8884659521433524)
        g.graph.add_edge(1, 2, 1.8884659521433524)
        g.graph.add_edge(2, 3, 1.7155926739282625)
        g.graph.add_edge(3, 2, 1.143544758336538)
        g.graph.add_edge(3, 2, 1.0980094622804095)
        g.graph.add_edge(3, 4, 1.4301580756736283)
        g.graph.add_edge(4, 3, 1.4899867265011255)
        g.graph.add_edge(4, 5, 1.9442789961315767)
        g.graph.add_edge(5, 4, 1.4622464066335845)
        g.graph.add_edge(5, 6, 1.160662656360925)
        g.graph.add_edge(6, 5, 1.6677173820549975)
        g.graph.add_edge(7, 6, 1.0176531013725074)
        g.graph.add_edge(6, 7, 1.3968360163668776)
        g.graph.add_edge(7, 8, 1.354895648936991)
        g.graph.add_edge(8, 7, 1.6449953452844968)
        g.graph.add_edge(8, 9, 1.8526880332753517)
        g.graph.add_edge(9, 8, 1.4575484853801393)
        g.graph.add_edge(9, 10, 1.022651770039933)
        g.graph.add_edge(10, 0, 1.1761238717867548)
        g.graph.add_edge(10, 9, 1.0887225789883779)

        self.assertEqual(g.shortest_path(0, 1), [1.4004465106761335, [0, 1]])

    # def test_lowest_dist(self):
    #
    # def test_Dijkstra_algorithm_path(self):
    #

    def test_TSP(self):
        g = GraphAlgo()
        for n in range(10):
            g.graph.add_node(n)

        g.graph.add_edge(0, 1, 1.4004465106761335)
        g.graph.add_edge(0, 10, 1.4620268165085584)
        g.graph.add_edge(1, 0, 1.8884659521433524)
        g.graph.add_edge(1, 2, 1.8884659521433524)
        g.graph.add_edge(2, 3, 1.7155926739282625)
        g.graph.add_edge(3, 2, 1.143544758336538)
        g.graph.add_edge(3, 2, 1.0980094622804095)
        g.graph.add_edge(3, 4, 1.4301580756736283)
        g.graph.add_edge(4, 3, 1.4899867265011255)
        g.graph.add_edge(4, 5, 1.9442789961315767)
        g.graph.add_edge(5, 4, 1.4622464066335845)
        g.graph.add_edge(5, 6, 1.160662656360925)
        g.graph.add_edge(6, 5, 1.6677173820549975)
        g.graph.add_edge(7, 6, 1.0176531013725074)
        g.graph.add_edge(6, 7, 1.3968360163668776)
        g.graph.add_edge(7, 8, 1.354895648936991)
        g.graph.add_edge(8, 7, 1.6449953452844968)
        g.graph.add_edge(8, 9, 1.8526880332753517)
        g.graph.add_edge(9, 8, 1.4575484853801393)
        g.graph.add_edge(9, 10, 1.022651770039933)
        g.graph.add_edge(10, 0, 1.1761238717867548)
        g.graph.add_edge(10, 9, 1.0887225789883779)

        self.assertEqual(g.TSP([1, 3, 3, 4, 4, 5, 3, 8, 10, 8]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_centerPoint(self):
        g = GraphAlgo()
        for n in range(10):
            g.graph.add_node(n)

        g.graph.add_edge(0, 1, 1.4004465106761335)
        g.graph.add_edge(0, 10, 1.4620268165085584)
        g.graph.add_edge(1, 0, 1.8884659521433524)
        g.graph.add_edge(1, 2, 1.8884659521433524)
        g.graph.add_edge(2, 3, 1.7155926739282625)
        g.graph.add_edge(3, 2, 1.143544758336538)
        g.graph.add_edge(3, 2, 1.0980094622804095)
        g.graph.add_edge(3, 4, 1.4301580756736283)
        g.graph.add_edge(4, 3, 1.4899867265011255)
        g.graph.add_edge(4, 5, 1.9442789961315767)
        g.graph.add_edge(5, 4, 1.4622464066335845)
        g.graph.add_edge(5, 6, 1.160662656360925)
        g.graph.add_edge(6, 5, 1.6677173820549975)
        g.graph.add_edge(7, 6, 1.0176531013725074)
        g.graph.add_edge(6, 7, 1.3968360163668776)
        g.graph.add_edge(7, 8, 1.354895648936991)
        g.graph.add_edge(8, 7, 1.6449953452844968)
        g.graph.add_edge(8, 9, 1.8526880332753517)
        g.graph.add_edge(9, 8, 1.4575484853801393)
        g.graph.add_edge(9, 10, 1.022651770039933)
        g.graph.add_edge(10, 0, 1.1761238717867548)
        g.graph.add_edge(10, 9, 1.0887225789883779)

        self.assertEqual(g.centerPoint(), (7, 6.806805834715163))

    def test_is_connected(self):
        g = GraphAlgo()
        for n in range(10):
            g.graph.add_node(n)

        g.graph.add_edge(0, 1, 1.4004465106761335)
        g.graph.add_edge(0, 10, 1.4620268165085584)
        g.graph.add_edge(1, 0, 1.8884659521433524)
        g.graph.add_edge(1, 2, 1.8884659521433524)
        g.graph.add_edge(2, 3, 1.7155926739282625)
        g.graph.add_edge(3, 2, 1.143544758336538)
        g.graph.add_edge(3, 2, 1.0980094622804095)
        g.graph.add_edge(3, 4, 1.4301580756736283)
        g.graph.add_edge(4, 3, 1.4899867265011255)
        g.graph.add_edge(4, 5, 1.9442789961315767)
        g.graph.add_edge(5, 4, 1.4622464066335845)
        g.graph.add_edge(5, 6, 1.160662656360925)
        g.graph.add_edge(6, 5, 1.6677173820549975)
        g.graph.add_edge(7, 6, 1.0176531013725074)
        g.graph.add_edge(6, 7, 1.3968360163668776)
        g.graph.add_edge(7, 8, 1.354895648936991)
        g.graph.add_edge(8, 7, 1.6449953452844968)
        g.graph.add_edge(8, 9, 1.8526880332753517)
        g.graph.add_edge(9, 8, 1.4575484853801393)
        g.graph.add_edge(9, 10, 1.022651770039933)
        g.graph.add_edge(10, 0, 1.1761238717867548)
        g.graph.add_edge(10, 9, 1.0887225789883779)

        self.assertTrue(g.is_connected())

    # def test_plot_graph(self):


if __name__ == '__main__':
    unittest.main()
