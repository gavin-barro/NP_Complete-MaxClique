class Vertex:

    def __init__(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def num_neighbors(self):
        return self.neighbors.len()
