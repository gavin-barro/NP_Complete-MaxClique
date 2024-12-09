# TODO: add to test case file or delete before submitting:

# def temp_tests() -> None:
    
#     def print_test_case(description: str, graph: dict[str, list[str]], expected: list[str]):
#         actual = find_max_clique_exact(graph)
#         print(f"Test: {description}")
#         print(f"Graph: {graph}")
#         print(f"Expected: {format_graph(expected)}")
#         print(f"Actual: {format_graph(actual)}")
#         print("-" * 40)

#     # Basic test cases
#     print_test_case(
#         "Basic test with a graph with two cliques",
#         {
#             'A': ['B', 'C'],
#             'B': ['A', 'C', 'F'],
#             'C': ['A', 'B', 'G'],
#             'D': ['E', 'F', 'G'],
#             'E': ['D', 'F', 'G'],
#             'F': ['D', 'E', 'G'],
#             'G': ['D', 'E', 'F']
#         },
#         ['D', 'E', 'F', 'G']
#     )

#     # Edge Case 1: Empty Graph
#     print_test_case(
#         "Empty graph",
#         {},
#         []
#     )

#     # Edge Case 2: Single Vertex
#     print_test_case(
#         "Single vertex",
#         {'A': []},
#         ['A']
#     )

#     # Edge Case 3: Two Connected Vertices
#     print_test_case(
#         "Two connected vertices",
#         {
#             'A': ['B'],
#             'B': ['A']
#         },
#         ['A', 'B']
#     )

#     # Edge Case 4: Disconnected Graph
#     print_test_case(
#         "Disconnected graph",
#         {
#             'A': ['B'],
#             'B': ['A'],
#             'C': ['D'],
#             'D': ['C']
#         },
#         ['A', 'B']  # Or ['C', 'D'], depending on traversal order
#     )

#     # Edge Case 5: Fully Connected Graph
#     print_test_case(
#         "Fully connected graph",
#         {
#             'A': ['B', 'C', 'D'],
#             'B': ['A', 'C', 'D'],
#             'C': ['A', 'B', 'D'],
#             'D': ['A', 'B', 'C']
#         },
#         ['A', 'B', 'C', 'D']
#     )

#     # Edge Case 6: Bipartite Graph
#     print_test_case(
#         "Bipartite graph",
#         {
#             'A': ['C', 'D'],
#             'B': ['C', 'D'],
#             'C': ['A', 'B'],
#             'D': ['A', 'B']
#         },
#         ['A', 'C']  # Or ['B', 'D'], depending on traversal order
#     )

#     # Edge Case 7: Star Graph
#     print_test_case(
#         "Star graph",
#         {
#             'A': ['B', 'C', 'D', 'E'],
#             'B': ['A'],
#             'C': ['A'],
#             'D': ['A'],
#             'E': ['A']
#         },
#         ['A', 'B']  # Or any other neighbor of A
#     )

#     # Edge Case 8: Graph with Multiple Cliques
#     print_test_case(
#         "Graph with multiple cliques",
#         {
#             'A': ['B', 'C'],
#             'B': ['A', 'C'],
#             'C': ['A', 'B'],
#             'D': ['E', 'F'],
#             'E': ['D', 'F'],
#             'F': ['D', 'E'],
#             'G': []
#         },
#         ['A', 'B', 'C']  # Or ['D', 'E', 'F'], depending on traversal order
#     )

#     # Edge Case 9: Path Graph
#     print_test_case(
#         "Path graph",
#         {
#             'A': ['B'],
#             'B': ['A', 'C'],
#             'C': ['B', 'D'],
#             'D': ['C']
#         },
#         ['A', 'B']  # Or ['B', 'C'] or ['C', 'D'], depending on traversal order
#     )