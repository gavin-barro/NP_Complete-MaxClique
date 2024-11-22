# Implemenation of Ford-Fulkerson
# Author: John C. Bowers
# Date: Dec. 5, 2023

from collections import deque

# The capacity function c is given as a dictionary of dictionaries.
# Where c[u][v] is the capacity of the edge from u to v.
#
# The source s and sink t are given as vertices.
def max_flow(c, s, t):
    f = {u: {v: 0 for v in c[u]} for u in c}
    Gf = residual_graph(c, f)
    path = augmenting_path(Gf, s, t)
    while path is not None:
        bottleneck = min(Gf[u][v] for u, v in zip(path, path[1:]))
        augment(f, path, bottleneck)
        Gf = residual_graph(c, f)
        path = augmenting_path(Gf, s, t)
    return f

def residual_graph(c, f):
    Gf = {u: {} for u in c}
    for u in c:
        for v in c[u]:
            if f[u][v] < c[u][v]:
                Gf[u][v] = c[u][v] - f[u][v]
            if f[u][v] > 0:
                Gf[v][u] = f[u][v]
    return Gf

def bfs(G, s):
    Q = deque([(None, s)])
    marked = set()
    parent = {}
    while Q: 
        p, v = Q.popleft()
        if v not in marked:
            marked.add(v)
            parent[v] = p
            for w in G[v]:
                Q.append((v, w))
    return marked, parent

def augmenting_path(Gf, s, t):
    marked, parent = bfs(Gf, s)
    if t not in marked:
        return None
    path = [t]
    while path[-1] != s:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def augment(f, path, bottleneck):
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        if v in f[u]:
            f[u][v] += bottleneck
        else:
            f[v][u] -= bottleneck

def flow_value(f, s):
    return sum(f[s][v] for v in f[s])