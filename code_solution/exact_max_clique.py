import time
import sys

# Set the recursion limit to a higher number, e.g., 5000
sys.setrecursionlimit(5000)

# Key: the nodes themselves
# Value: The nodes' neightbors that are connected with an edge
Graph = dict[str, list[str]]


def is_clique(graph, vertices) -> bool:
    for v in vertices:  # loops through vertices
        for u in vertices:  # loops through every other vertex in the graph
            # sees if first vertex is different than other vertex and if the first vertex is not a niehgbor of the second
            if u != v and u not in graph[v]:
                return False  # if the pair of vertices aren't connected than they aren't in a clique
    return True  # if all vertices are connected they are a clique


def backtrack_max_clique(graph: Graph, candidates: list[str], current_clique: list[str], 
                         best_clique: list[list]) -> None:
    # If no candidates left or no larger clique possible, return best found so far
    if not candidates:
        # Check if current_clique is the largest so far
        if len(current_clique) > len(best_clique[0]):
            best_clique[0] = current_clique[:]
        return

    # If current clique + candidates count <= size of best clique, no need to proceed
    if len(current_clique) + len(candidates) <= len(best_clique[0]):
        return

    while candidates:
        v = candidates.pop()
        # Check if v can be added to current_clique
        # v must be connected to all vertices in current_clique
        if all((u in graph[v]) for u in current_clique):
            # Narrow down next candidates to only those connected to v
            new_candidates = [u for u in candidates if u in graph[v]]
            current_clique.append(v)
            backtrack_max_clique(graph, new_candidates,
                                 current_clique, best_clique)
            current_clique.pop()
        # Even if v doesn't fit try the next candidate


def find_max_clique_exact(graph: Graph) -> list:
    vertices = list(graph.keys())
    best_clique = [[]]  # Using a list so it can be updated in recursion
    backtrack_max_clique(graph, vertices, [], best_clique)
    return best_clique[0]


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
    return " ".join(clique)
    
def generate_large_graph(num_vertices: int) -> dict:
    """Generates a large random graph."""
    graph = {str(i): [] for i in range(num_vertices)}  # Create vertices labeled 0, 1, 2, ..., num_vertices-1
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Avoid self-loops
            graph[str(i)].append(str(j))
            graph[str(j)].append(str(i))
    return graph

def worst_case_graph() -> None:
    num_vertices = 1125 
    start_time = time.time()

    # Generate large graph and find max clique
    large_graph = generate_large_graph(num_vertices)
    max_clique = find_max_clique_exact(large_graph)
    end_time = time.time()

    # Calculate the time
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    print("Max clique:", format_graph(max_clique))
    print(f"Time taken: {minutes} minutes and {seconds} seconds")
 


def main() -> None:
    # Testing generate graph function
    # num_edges = input("How any edges are there (list an int): ")
    # edges = []
    # for _ in range(int(num_edges)):
    #     edge = input("List an edge (ex. A B): ")
    #     edges.append(edge)
    # example_graph = generate_graph(edges)
    # max_clique_exact = find_max_clique_exact(example_graph)
    # print("Max clique: ", format_graph(max_clique_exact))

    # Very large graph that would take a LOT of time to run
    worst_case_graph()


if __name__ == "__main__":
    main()
