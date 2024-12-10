import unittest
import random
from max_clique import Graph
import approximate_max_clique as approx
import exact_max_clique as exact
import known_max_clique as known
from collections import Counter


def random_graph(num_vertices, edge_probability=0.5):
    vertices = [chr(ord('A') + i) for i in range(num_vertices)]
    edges = []
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() < edge_probability:
                edges.append(vertices[i] + " " + vertices[j])
    return edges


class TestMaxCliqueMethods(unittest.TestCase):

    def test_random_graphs(self):
        # run this test multiple times to check different graphs
        random.seed(42)

        for _ in range(5):
            edges = random_graph(num_vertices=6, edge_probability=0.3)

            # Preprocess edges for the known solution
            # Reset global variables in `known_max_clique`
            known.graph = [[0 for _ in range(100)] for _ in range(100)]
            known.n = 0

            vertex_map = {}
            current_id = 1
            for edge in edges:
                u, v = edge.split()
                if u.upper() not in vertex_map:
                    vertex_map[u.upper()] = current_id
                    current_id += 1
                if v.upper() not in vertex_map:
                    vertex_map[v.upper()] = current_id
                    current_id += 1

            known.n = len(vertex_map)

            for edge in edges:
                u, v = edge.split()
                u_id = vertex_map[u.upper()]
                v_id = vertex_map[v.upper()]
                known.graph[u_id][v_id] = 1
                known.graph[v_id][u_id] = 1

            # Expected solution (size only)
            expected_size = known.maxCliques(0, 1)

            # Exact solution (should return actual clique)
            exact_graph = exact.generate_graph(edges)
            exact_clique = exact.find_max_clique_exact(exact_graph)
            exact_size = len(exact_clique)

            # Approx solution
            approx_graph = approx.generate_graph(edges)
            approx_clique = approx.find_max_clique_approx(approx_graph)
            approx_size = len(approx_clique)

            # The expected and exact solutions should match exactly in size
            self.assertEqual(expected_size, exact_size,
                             f"Expected size {expected_size}, got {exact_size} for edges {edges}")

            self.assertLessEqual(approx_size, exact_size,
                                 "Approx solution found clique larger than the exact solution")


def test_find_max_clique() -> None:
    # Basic test cases
    graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'F'],
        'C': ['A', 'B', 'G'],
        'D': ['E', 'F', 'G'],
        'E': ['D', 'F', 'G'],
        'F': ['D', 'E', 'G'],
        'G': ['D', 'E', 'F']
    }
    max_clique = exact.find_max_clique_exact(graph1)
    assert Counter(max_clique) == Counter(
        ['D', 'E', 'F', 'G']), "Test Case 1 Failed"

    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['C', 'E'],
        'E': ['C', 'D']
    }
    assert Counter(exact.find_max_clique_exact(graph2)) == Counter(
        ['E', 'D', 'C']), "Test Case 2 Failed"

    graph3 = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b']
    }
    assert Counter(exact.find_max_clique_exact(graph3)) == Counter(
        ['a', 'b', 'c']), "Test Case 3 Failed"

    graph4 = {
        'a': ['b'],
        'b': ['a', 'c', 'd'],
        'c': ['b', 'd'],
        'd': ['b', 'c']
    }
    assert Counter(exact.find_max_clique_exact(graph4)) == Counter(
        ['b', 'c', 'd']), "Test Case 4 Failed"

    graph5 = {
        'a': ['b', 'c'],
        'b': ['a'],
        'c': ['a']
    }
    assert Counter(exact.find_max_clique_exact(graph5)) == Counter(
        ['a', 'c']), "Test Case 5 Failed"

    # Edge case tests
    graph6 = {}
    assert Counter(exact.find_max_clique_exact(graph6)
                   ) == Counter([]), "Empty Graph Test Failed"

    graph7 = {'a': []}
    assert Counter(exact.find_max_clique_exact(graph7)) == Counter(
        ['a']), "Single Vertex Test Failed"

    graph8 = {
        'a': ['b'],
        'b': ['a']
    }
    assert Counter(exact.find_max_clique_exact(graph8)) == Counter(
        ['a', 'b']), "Single Edge Test Failed"

    graph9 = {
        'a': ['b'],
        'b': ['a'],
        'c': [],
        'd': []
    }
    assert Counter(exact.find_max_clique_exact(graph9)) == Counter(
        ['a', 'b']), "Disconnected Graph Test Failed"

    graph10 = {
        'a': ['b'],
        'b': ['a', 'c'],
        'c': ['b', 'd'],
        'd': ['c']
    }

    assert Counter(exact.find_max_clique_exact(graph10)) == Counter(
        ['c', 'd']), "Chain of Vertices Test Failed"

    graph11 = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b']
    }
    assert Counter(exact.find_max_clique_exact(graph11)) == Counter(
        ['a', 'b', 'c']), "Triangle Test Failed"

    graph12 = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd'],
        'd': ['a', 'b', 'c']
    }
    assert Counter(exact.find_max_clique_exact(graph12)) == Counter(
        ['a', 'b', 'c', 'd']), "Complete Graph Test Failed"

    graph13 = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd'],
        'd': ['b', 'c'],
        'e': ['f'],
        'f': ['e']
    }

    assert Counter(exact.find_max_clique_exact(graph13)) == Counter(
        ['d', 'b', 'c']), "Larger Graph Test Failed"

    graph14 = {
        'a': ['b'],
        'b': ['a'],
        'c': ['d'],
        'd': ['c'],
        'e': []
    }

    assert Counter(exact.find_max_clique_exact(graph14)) == Counter(
        ['d', 'c']), "Graph with Isolated Vertices Test Failed"

    graph15 = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd'],
        'd': ['b', 'c']
    }

    assert Counter(exact.find_max_clique_exact(graph15)) == Counter(
        ['d', 'c']), "Complete Bipartite Graph Test Failed"

    graph16 = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
        'd': ['a']
    }
    assert Counter(exact.find_max_clique_exact(graph16)) == Counter(
        ['a', 'b', 'c']), "Fully Connected Subgraphs Test Failed"

    print("All test cases passed!")


# Run the test cases
test_find_max_clique()


if __name__ == '__main__':
    unittest.main()
