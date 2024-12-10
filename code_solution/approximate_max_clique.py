import sys

# Set the recursion limit to a higher number
sys.setrecursionlimit(5000)

# Key: the nodes themselves
# Value: The nodes' neighbors that are connected with an edge
Graph = dict[str, list[str]]


def is_clique(graph, vertices) -> bool:
    for v in vertices:
        for u in vertices:
            if u != v and u not in graph[v]:
                return False
    return True


def find_max_clique_approx(graph: Graph) -> list[str]:
    if not graph:
        return []

    vertices = sorted(graph.keys(), key=lambda v: len(graph[v]), reverse=True)

    best_clique = []
    for vertex in vertices:
        clique = [vertex]
        candidates = list(graph[vertex])

        while candidates:
            candidates.sort(key=lambda c: len(graph[c]), reverse=True)
            chosen = None
            for c in candidates:
                if all((c in graph[u]) for u in clique):
                    chosen = c
                    break
            if chosen:
                clique.append(chosen)

                candidates = [
                    u for u in candidates if u in graph[chosen] and u != chosen]
            else:
                break

        if len(clique) > len(best_clique):
            best_clique = clique

    return best_clique


def generate_graph(edges: list[str]) -> Graph:
    graph = {}
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
    return " ".join(clique)


def main() -> None:
    num_edges = input("How any edges are there (list an int): ")
    edges = []
    for _ in range(int(num_edges)):
        edge = input("List an edge (ex. A B): ")
        edges.append(edge)
    example_graph = generate_graph(edges)
    max_clique_approx = find_max_clique_approx(example_graph)
    print("Max clique: ", format_graph(max_clique_approx))


if __name__ == "__main__":
    main()
