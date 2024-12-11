from max_clique import Graph
import exact_max_clique as exact
import time
import sys

# Set the recursion limit to a higher number
sys.setrecursionlimit(5000)

def generate_worst_case_graph(num_vertices: int) -> Graph:
    graph = {str(i): [] for i in range(num_vertices)}  # Create vertices labeled 0, 1, 2, ..., num_vertices-1
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Avoid self-loops
            graph[str(i)].append(str(j))
            graph[str(j)].append(str(i))
    return graph

def worst_case_graph() -> None:
    num_vertices = 1200 
    start_time = time.time()

    # Generate large graph and find max clique
    large_graph = generate_worst_case_graph(num_vertices)
    max_clique = exact.find_max_clique_exact(large_graph)
    end_time = time.time()

    # Calculate the time
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    print("Max clique:", exact.format_graph(max_clique))
    print(f"Time taken: {minutes} minutes and {seconds} seconds")
    
def main() -> None:
    worst_case_graph()   
    
if __name__ == "__main__":
    main()