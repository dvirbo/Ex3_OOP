import unittest

from classes.DiGraph import DiGraph
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

    def test_TSP(self):
        g = DiGraph()
        for n in range(11):
            g.add_node(n)

        g.add_edge(0, 1, 1.4004465106761335)
        g.add_edge(0, 10, 1.4620268165085584)
        g.add_edge(1, 0, 1.8884659521433524)
        g.add_edge(1, 2, 1.8884659521433524)
        g.add_edge(2, 3, 1.7155926739282625)
        g.add_edge(3, 2, 1.143544758336538)
        g.add_edge(3, 2, 1.0980094622804095)
        g.add_edge(3, 4, 1.4301580756736283)
        g.add_edge(4, 3, 1.4899867265011255)
        g.add_edge(4, 5, 1.9442789961315767)
        g.add_edge(5, 4, 1.4622464066335845)
        g.add_edge(5, 6, 1.160662656360925)
        g.add_edge(6, 5, 1.6677173820549975)
        g.add_edge(7, 6, 1.0176531013725074)
        g.add_edge(6, 7, 1.3968360163668776)
        g.add_edge(7, 8, 1.354895648936991)
        g.add_edge(8, 7, 1.6449953452844968)
        g.add_edge(8, 9, 1.8526880332753517)
        g.add_edge(9, 8, 1.4575484853801393)
        g.add_edge(9, 10, 1.022651770039933)
        g.add_edge(10, 0, 1.1761238717867548)
        g.add_edge(10, 9, 1.0887225789883779)

        graphA = GraphAlgo(g)
        self.assertEqual(graphA.TSP([1, 3, 3, 4, 4, 5, 3, 8, 10, 8]), ([1, 0, 10, 9, 8, 7, 6, 5, 4, 3], 38.99149475980027))

        g2 = DiGraph()
        for n in range(11):
            g2.add_node(n)

        g2.add_edge(1, 0, 1.8884659521433524)
        g2.add_edge(1, 2, 1.8884659521433524)
        g2.add_edge(2, 3, 1.7155926739282625)
        g2.add_edge(3, 2, 1.143544758336538)
        g2.add_edge(3, 2, 1.0980094622804095)
        g2.add_edge(3, 4, 1.4301580756736283)
        g2.add_edge(4, 3, 1.4899867265011255)
        g2.add_edge(4, 5, 1.9442789961315767)
        g2.add_edge(5, 4, 1.4622464066335845)
        g2.add_edge(5, 6, 1.160662656360925)
        g2.add_edge(6, 5, 1.6677173820549975)
        g2.add_edge(7, 6, 1.0176531013725074)
        g2.add_edge(6, 7, 1.3968360163668776)
        g2.add_edge(7, 8, 1.354895648936991)
        g2.add_edge(8, 7, 1.6449953452844968)
        g2.add_edge(8, 9, 1.8526880332753517)
        g2.add_edge(9, 8, 1.4575484853801393)

        graphA2 = GraphAlgo(g2)
        self.assertEqual(graphA2.TSP([1, 3, 3, 4, 4, 5, 3, 8, 10, 8]),
                         (-1, float('inf')))

    def test_centerPoint(self):
        g = DiGraph()
        for n in range(11):
            g.add_node(n)

        g.add_edge(0, 1, 1.4004465106761335)
        g.add_edge(0, 10, 1.4620268165085584)
        g.add_edge(1, 0, 1.8884659521433524)
        g.add_edge(1, 2, 1.8884659521433524)
        g.add_edge(2, 3, 1.7155926739282625)
        g.add_edge(3, 2, 1.143544758336538)
        g.add_edge(3, 2, 1.0980094622804095)
        g.add_edge(3, 4, 1.4301580756736283)
        g.add_edge(4, 3, 1.4899867265011255)
        g.add_edge(4, 5, 1.9442789961315767)
        g.add_edge(5, 4, 1.4622464066335845)
        g.add_edge(5, 6, 1.160662656360925)
        g.add_edge(6, 5, 1.6677173820549975)
        g.add_edge(7, 6, 1.0176531013725074)
        g.add_edge(6, 7, 1.3968360163668776)
        g.add_edge(7, 8, 1.354895648936991)
        g.add_edge(8, 7, 1.6449953452844968)
        g.add_edge(8, 9, 1.8526880332753517)
        g.add_edge(9, 8, 1.4575484853801393)
        g.add_edge(9, 10, 1.022651770039933)
        g.add_edge(10, 0, 1.1761238717867548)
        g.add_edge(10, 9, 1.0887225789883779)

        graphA = GraphAlgo(g)
        self.assertEqual(graphA.centerPoint(), (7, 6.806805834715163))

        g2 = DiGraph()
        for n in range(11):
            g2.add_node(n)

        g2.add_edge(1, 0, 1.8884659521433524)
        g2.add_edge(1, 2, 1.8884659521433524)
        g2.add_edge(2, 3, 1.7155926739282625)
        g2.add_edge(3, 2, 1.143544758336538)
        g2.add_edge(3, 2, 1.0980094622804095)
        g2.add_edge(3, 4, 1.4301580756736283)
        g2.add_edge(4, 3, 1.4899867265011255)
        g2.add_edge(4, 5, 1.9442789961315767)
        g2.add_edge(5, 4, 1.4622464066335845)
        g2.add_edge(5, 6, 1.160662656360925)
        g2.add_edge(6, 5, 1.6677173820549975)
        g2.add_edge(7, 6, 1.0176531013725074)
        g2.add_edge(6, 7, 1.3968360163668776)
        g2.add_edge(7, 8, 1.354895648936991)
        g2.add_edge(8, 7, 1.6449953452844968)
        g2.add_edge(8, 9, 1.8526880332753517)
        g2.add_edge(9, 8, 1.4575484853801393)

        graphA2 = GraphAlgo(g2)

        self.assertEqual(graphA2.centerPoint(), (-1, float('inf')))

    def test_is_connected(self):
        g = GraphAlgo()
        for n in range(11):
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

        g2 = GraphAlgo()
        for n in range(11):
            g2.graph.add_node(n)

        g2.graph.add_edge(0, 1, 1.4004465106761335)
        g2.graph.add_edge(1, 0, 1.8884659521433524)
        g2.graph.add_edge(1, 2, 1.8884659521433524)
        g2.graph.add_edge(2, 3, 1.7155926739282625)
        g2.graph.add_edge(3, 2, 1.143544758336538)
        g2.graph.add_edge(3, 2, 1.0980094622804095)
        g2.graph.add_edge(3, 4, 1.4301580756736283)
        g2.graph.add_edge(4, 3, 1.4899867265011255)
        g2.graph.add_edge(4, 5, 1.9442789961315767)
        g2.graph.add_edge(5, 4, 1.4622464066335845)
        g2.graph.add_edge(5, 6, 1.160662656360925)
        g2.graph.add_edge(6, 5, 1.6677173820549975)
        g2.graph.add_edge(7, 6, 1.0176531013725074)
        g2.graph.add_edge(6, 7, 1.3968360163668776)
        g2.graph.add_edge(7, 8, 1.354895648936991)
        g2.graph.add_edge(8, 7, 1.6449953452844968)
        g2.graph.add_edge(8, 9, 1.8526880332753517)
        g2.graph.add_edge(9, 8, 1.4575484853801393)

        self.assertFalse(g2.is_connected())


if __name__ == '__main__':
    unittest.main()
