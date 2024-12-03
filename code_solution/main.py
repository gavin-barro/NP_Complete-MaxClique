
graph = {'A': ['B', 'C'],
         'B': ['A', 'C'],
         'C': ['A', 'B']
         }


def solver(graph G):
    biggest_clique = []
    for v in G:
        for e in v:
            if e in biggest_clique:


def main() -> None:
    pass


if __name__ == "__main__":
    main()
