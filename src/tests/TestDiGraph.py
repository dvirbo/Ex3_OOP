import unittest


class MyTestCase(unittest.TestCase):
    def test_v_size(self):

    def test_e_size(self):

    def test_get_all_v(self):

    def test_all_in_edges_of_node(self, id1: int):

    def test_all_out_edges_of_node(self, id1: int):

    def test_get_mc(self):

    def test_contains(self, key):

    def test_add_edge(self, id1: int, id2: int, weight: float):

    def test_add_node(self, node_id: int, pos: tuple = None):

    def test_getNode(self, key: int):

    def test_remove_node(self, node_id: int):

    def test_remove_edge(self, node_id1: int, node_id2: int):

    def test_get_edge(self, id1: int, id2: int):


if __name__ == '__main__':
    unittest.main()
