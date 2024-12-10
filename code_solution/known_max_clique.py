import sys
sys.setrecursionlimit(5000)

MAX = 100
n = 0

# Global arrays used by maxCliques and is_clique
store = [0] * MAX
graph = [[0 for _ in range(MAX)] for _ in range(MAX)]
d = [0] * MAX


def is_clique(b):
    for i in range(1, b):
        for j in range(i + 1, b):
            if (graph[store[i]][store[j]] == 0):
                return False
    return True


def maxCliques(i, l):
    max_ = 0
    for j in range(i + 1, n + 1):
        store[l] = j
        if (is_clique(l + 1)):
            max_ = max(max_, l)
            max_ = max(max_, maxCliques(j, l + 1))
    return max_


def main():
    num_edges = input("How any edges are there (list an int): ")
    edges = []
    for _ in range(int(num_edges)):
        edge = input("List an edge (ex. A B): ")
        edges.append(edge.strip().split())

    vertex_map = {}
    current_id = 1
    for u, v in edges:
        if u.upper() not in vertex_map:
            vertex_map[u.upper()] = current_id
            current_id += 1
        if v.upper() not in vertex_map:
            vertex_map[v.upper()] = current_id
            current_id += 1

    global n
    n = len(vertex_map)

    for u, v in edges:
        u_id = vertex_map[u.upper()]
        v_id = vertex_map[v.upper()]
        graph[u_id][v_id] = 1
        graph[v_id][u_id] = 1
        d[u_id] += 1
        d[v_id] += 1

    max_clique_size = maxCliques(0, 1)

    print("Max clique size:", max_clique_size)


if __name__ == "__main__":
    main()
