
graph = {'A': ['B', 'C'],
         'B': ['A', 'C'],
         'C': ['A', 'B']
         }

Graph = dict[str, list[str]]


# def solver(G: Graph):
#     biggest_clique = []
#     for v, e in G:
#         for e in v.values():
#             if e in biggest_clique:


def main() -> None:
    graph = {'A': ['B', 'C'],
         'B': ['A', 'C'],
         'C': ['A', 'B']
         }
    
    for v, e in graph.items():
        print(f"Vertex: {v}")
        print(f"Edge: {e}")
        print('----')


if __name__ == "__main__":
    main()
