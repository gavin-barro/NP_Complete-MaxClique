from max_clique import Graph
import approximate_max_clique as approx
import exact_max_clique as exact
import random
import time
import matplotlib.pyplot as plt
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
    

def generate_plot_graph(num_vertices: int) -> Graph:
    graph = {str(i): [] for i in range(num_vertices)}  # Create vertices labeled 0, 1, 2, ..., num_vertices-1
    edge_count = 0  # Initialize edge counter
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Avoid self-loops
            if random.random() < 0.5:  # 50% chance of adding an edge
                graph[str(i)].append(str(j))
                graph[str(j)].append(str(i))
                edge_count += 1  # Increment edge counter for each edge added
    return graph, edge_count  # Return the graph and the edge count


def plot_graph(num_vertices: int) -> None:
    # Generate the graph with num_vertices
    large_graph, edge_count = generate_plot_graph(num_vertices)
    
    # Measure time for Exact Algorithm
    start_time = time.time()
    max_clique = exact.find_max_clique_exact(large_graph)
    end_time = time.time()
    exact_time = end_time - start_time
    
    # Measure time for Approximate Algorithm
    start_time = time.time()
    max_clique = approx.find_max_clique_approx(large_graph)
    end_time = time.time()
    approx_time = end_time - start_time
    
    # Print out results
    print(f"Exact Max Clique: {exact.format_graph(max_clique)}")
    print(f"Time taken for Exact Algorithm: {exact_time:.6f} seconds")
    print(f"Approximate Max Clique: {approx.format_graph(max_clique)}")
    print(f"Time taken for Approximate Algorithm: {approx_time:.6f} seconds")
    print(f"Total number of edges: {edge_count}")

    return exact_time, approx_time  # Return times for later plotting


def main():
    # Data collection for runtime comparison
    runtimes = {'input_size': [], 'exact_runtime': [], 'approx_runtime': []}
    
    for num_vertices in range(100, 1000, 100):  # Test graph sizes from 10 to 100 vertices, increasing by 10
        print(f"Testing with {num_vertices} vertices...")
        exact_time, approx_time = plot_graph(num_vertices)  # Measure the times
        runtimes['input_size'].append(num_vertices)
        runtimes['exact_runtime'].append(exact_time)
        runtimes['approx_runtime'].append(approx_time)
    
    # Plot the runtime comparison
    plt.figure(figsize=(10, 6))
    plt.plot(runtimes['input_size'], runtimes['exact_runtime'], label='Exact Algorithm', color='blue', marker='o')
    plt.plot(runtimes['input_size'], runtimes['approx_runtime'], label='Approximate Algorithm', color='red', marker='x')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (Seconds)')
    plt.title('Runtime Comparison: Exact vs Approximate Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == '__main__':
    main()