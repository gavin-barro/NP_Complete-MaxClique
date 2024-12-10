import unittest
import random
from max_clique import Graph
import approximate_max_clique as approx
import exact_max_clique as exact
import known_max_clique as known


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


if __name__ == '__main__':
    unittest.main()
