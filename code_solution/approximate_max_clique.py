from typing import List, Dict

# Key: the nodes themselves
# Value: The nodes' neightbors that are connected with an edge
Graph = dict[str, list[str]]


def is_clique(graph: Graph, vertices: List[str]) -> bool:
    for v in vertices:  # loops through vertices
        for u in vertices:  # loops through every other vertex in the graph
            # sees if first vertex is different than other vertex and if the first vertex is not a niehgbor of the second
            if u != v and u not in graph[v]:
                return False  # if the pair of vertices aren't connected than they aren't in a clique
    return True  # if all vertices are connected they are a clique


def find_max_clique_approx(graph: Graph) -> List[str]:
    biggest_clique = []  # keeps track of biggest clique so far
    # sorts from highest to smallest in terms of vertices
    vertices = sorted(graph.keys(), key=lambda v: len(graph[v]), reverse=True)
    for vertex in vertices:  # loops thorugh the vertices
        neighbors = graph[vertex]  # gets the neighobrs of each vertex
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
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    return graph


def format_graph(clique: list[str]):
    return " ".join(clique)


def main() -> None:
    # Testing generate graph function
    num_edges = input("How any edges are there (list an int): ")
    edges = []
    for _ in range(int(num_edges)):
        edge = input("List an edge (ex. A B): ")
        edges.append(edge)
    example_graph = generate_graph(edges)
    max_clique_ex = find_max_clique_approx(example_graph)
    print("Max clique: ", format_graph(max_clique_ex))


if __name__ == "__main__":
    main()
