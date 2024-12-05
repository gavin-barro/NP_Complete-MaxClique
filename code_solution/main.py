from typing import List, Dict

# graph = {'A': ['B', 'C'],
#          'B': ['A', 'C'],
#          'C': ['A', 'B']
#          }

Graph = dict[str, list[str]]


def is_clique(graph: Graph, vertices: List[str]) -> bool:
    for v in vertices:  # loops through vertices
        for u in vertices:  # loops through every other vertex in the graph
            # sees if first vertex is different than other vertex and if the first vertex is not a niehgbor of the second
            if u != v and u not in graph[v]:
                return False  # if the pair of vertices aren't connected than they aren't in a clique
    return True  # if all vertices are connected they are a clique


def find_max_clique(graph: Graph) -> List[str]:
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


def main() -> None:
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'F'],
        'C': ['A', 'B', 'G'],
        'D': ['E', 'F', 'G'],
        'E': ['D', 'F', 'G'],
        'F': ['D', 'E', 'G'],
        'G': ['D', 'E', 'F']
    }
    max_clique = find_max_clique(graph)
    print("Max clique: ", max_clique)

    # for v, e in graph.items():
    #     print(f"Vertex: {v}")
    #     print(f"Edge: {e}")
    #     print('----')


if __name__ == "__main__":
    main()
