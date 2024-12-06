import unittest
import max_clique

class TestMaxClique(unittest.TestCase):

    def test_case_1(self):
        graph = {'a': ['b'], 'b': ['a']}
        expected_output = ['a', 'b']
        self.assertEqual(max_clique.find_max_clique(graph), expected_output)
        
        