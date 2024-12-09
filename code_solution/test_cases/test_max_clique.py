import unittest
from code_solution.exact_max_clique import generate_graph, find_max_clique_exact, format_graph
# from exact_max_clique import generate_graph as exact_generate_graph
# from approximate_max_clique import generate_graph as approximate_generate_graph
# from exact_max_clique import is_clique as exact_is_clique
# from approximate_max_clique import is_clique as approx_is_clique
# from exact_max_clique import find_max_clique_exact
# from exact_max_clique import format_graph


class TestMaxClique(unittest.TestCase):

    # def test_case_1(self):
    #     graph = {'a': ['b'], 'b': ['a']}
    #     expected_output = ['a', 'b']
    #     self.assertEqual(max_clique.find_max_clique(graph), expected_output)

    def test_case_2(self):
        input_data = """A B
A C
A D
A E
A F
A H
A J
A K
A L
A M
A N
A O
A P
A Q
A R
A S
A T
A U
A V
B C
B D
B F
B G
B H
B I
B K
B L
B M
B N
B O
B P
B Q
B R
B S
B T
B U
C D
C E
C G
C H
C I
C J
C K
C N
C O
C P
C Q
C R
C S
C T
C U
C V
D E
D F
D G
D J
D K
D L
D O
D P
D Q
D R
D S
D T
D U
E F
E G
E H
E I
E L
E M
E N
E O
E P
E Q
E R
E S
E U
E V
F G
F H
F I
F J
F M
F N
F O
F P
F Q
F R
F S
F T
F V
G H
G I
G J
G K
G L
G M
G P
G Q
G R
G S
G T
G U
H I
H J
H K
H L
H N
H O
H P
H Q
H R
H S
H T
H U
I J
I K
I L
I M
I N
I O
I Q
I R
I S
I V"""

        # Parse the input data into edges
        edges = input_data.splitlines()
        num_edges = len(edges)

        # Generate the graph and find the maximum clique
        example_graph = exact_generate_graph = (edges)
        max_clique_ex = find_max_clique_exact(example_graph)

        # Output the result
        actual = format_graph(max_clique_ex)
        print(actual)
        expected = """ A B
A C
A D
A E
A F
A H
A J
A K
A L
A M
A N
A O
A P
"""
        self.assertEqual(actual, expected)
