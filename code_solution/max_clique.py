import sys
import exact_max_clique as exact

# Key: the nodes themselves
# Value: The nodes' neighbors that are connected with an edge
Graph = dict[str, list[str]]

# Set the recursion limit to a higher number
sys.setrecursionlimit(5000)


def is_clique(graph: Graph, vertices: list[str]) -> bool:
    for v in vertices:  # loops through vertices
        for u in vertices:  # loops through every other vertex in the graph
            # sees if first vertex is different than other vertex and if the first vertex is not a niehgbor of the second
            if u != v and u not in graph[v]:
                return False  # if the pair of vertices aren't connected than they aren't in a clique
    return True  # if all vertices are connected they are a clique


def find_max_clique(graph: Graph) -> list[str]:
    biggest_clique = []  # keeps track of biggest clique so far
    # sorts from highest to smallest in terms of vertices
    vertices = sorted(graph.keys(), key=lambda v: len(graph[v]), reverse=True)
    for vertex in vertices:  # loops through the vertices
        neighbors = graph[vertex]  # gets the neighbors of each vertex
        # makes a kind of graph with the vertex and it's neighbors
        maybe_clique = [vertex] + neighbors
        # calls is_clique with that graph to see if that kind of graph is a clique
        if is_clique(graph, maybe_clique):
            # replaces the biggest clique so far if that graph is a clique and bigger
            if len(maybe_clique) > len(biggest_clique):
                biggest_clique = maybe_clique

    return biggest_clique


def generate_graph(edges: list[str]) -> Graph:
    graph = {}

    # Parse edges to build the graph
    for edge in edges:
        u, v = edge.split()
        if u.upper() not in graph:
            graph[u.upper()] = []
        if v.upper() not in graph:
            graph[v.upper()] = []
        graph[u.upper()].append(v.upper())
        graph[v.upper()].append(u.upper())

    return graph


def format_graph(clique: list[str]) -> str:
    format_clique = ""
    for v in clique:
        format_clique += v + " "
    return format_clique


def main() -> None:
    # Testing generate graph function
    # num_edges = input("How any edges are there (list an int): ")
    # edges = []
    # for _ in range(int(num_edges)):
    #     edge = input("List an edge (ex. A B): ")
    #     edges.append(edge)
    # example_graph = generate_graph(edges)
    # max_clique_ex = find_max_clique(example_graph)
    # print("Max clique: ", format_graph(max_clique_ex))

    # Basic test cases
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'F'],
        'C': ['A', 'B', 'G'],
        'D': ['E', 'F', 'G'],
        'E': ['D', 'F', 'G'],
        'F': ['D', 'E', 'G'],
        'G': ['D', 'E', 'F']
    }
    max_clique = exact.find_max_clique_exact(graph)
    print("Max clique: ", max_clique)

    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['C', 'E'],
        'E': ['C', 'D']
    }
    max_clique2 = exact.find_max_clique_exact(graph2)
    print("Max clique: ", max_clique2)

    graph3 = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b']
    }
    max_clique3 = exact.find_max_clique_exact(graph3)
    print("Max clique: ", max_clique3)

    graph4 = {
        'a': ['b'],
        'b': ['a', 'c', 'd'],
        'c': ['b', 'd'],
        'd': ['b', 'c']
    }
    max_clique4 = exact.find_max_clique_exact(graph4)
    print("Max clique: ", max_clique4)

    graph5 = {
        'a': ['b', 'c'],
        'b': ['a'],
        'c': ['a']
    }
    max_clique5 = exact.find_max_clique_exact(graph5)
    print("Max clique: ", max_clique5)

    # Begin edge case tests
    print("Edge cases: ")

    # Empty Graph
    graph6 = {}
    max_clique6 = exact.find_max_clique_exact(graph6)
    print("Max clique: ", max_clique6)

    # Single Vertex
    graph7 = {
        'a': []
    }
    max_clique7 = exact.find_max_clique_exact(graph7)
    print("Max clique: ", max_clique7)

    # Single Edge
    graph8 = {
        'a': ['b'],
        'b': ['a']
    }
    max_clique8 = exact.find_max_clique_exact(graph8)
    print("Max clique: ", max_clique8)

    # Disconnected Graph
    graph9 = {
        'a': ['b'],
        'b': ['a'],
        'c': [],
        'd': []
    }
    max_clique9 = exact.find_max_clique_exact(graph9)
    print("Max clique: ", max_clique9)

    # Chain of Vertices
    graph10 = {
        'a': ['b'],
        'b': ['a', 'c'],
        'c': ['b', 'd'],
        'd': ['c']
    }
    max_clique10 = exact.find_max_clique_exact(graph10)
    print("Max clique: ", max_clique10)

    # Triangle
    graph11 = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b']
    }
    max_clique11 = exact.find_max_clique_exact(graph11)
    print("Max clique: ", max_clique11)

    # Complete Graph
    graph12 = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd'],
        'd': ['a', 'b', 'c']
    }
    max_clique12 = exact.find_max_clique_exact(graph12)
    print("Max clique: ", max_clique12)

    # Larger Graph with Multiple Cliques
    graph13 = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd'],
        'd': ['b', 'c'],
        'e': ['f'],
        'f': ['e']
    }
    max_clique13 = exact.find_max_clique_exact(graph13)
    print("Max clique: ", max_clique13)

    # Graph with Isolated Vertices
    graph14 = {
        'a': ['b'],
        'b': ['a'],
        'c': ['d'],
        'd': ['c'],
        'e': []
    }
    max_clique14 = exact.find_max_clique_exact(graph14)
    print("Max clique: ", max_clique14)

    # Complete Bipartite Graph
    graph15 = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd'],
        'd': ['b', 'c']
    }
    max_clique15 = exact.find_max_clique_exact(graph15)
    print("Max clique: ", max_clique15)

    # Fully Connected Subgraphs
    graph16 = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
        'd': ['a']
    }
    max_clique16 = exact.find_max_clique_exact(graph16)
    print("Max clique: ", max_clique16)

#     # for v, e in graph.items():
#     #     print(f"Vertex: {v}")
#     #     print(f"Edge: {e}")
#     #     print('----')


if __name__ == "__main__":
    main()
