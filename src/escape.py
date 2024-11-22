from network_flow import *

def grid_graph(n):
    # Create an return grid graph with n vertices
    pass

def escape_network(n, terminals):
    # Create and return the n x n escape network 
    # with the given terminals
    # you may want to include source/sink vertices
    pass

def bfs_unit_flow(f, s):
    # Given a unitary flow (all values 1 or 0), 
    # find a path from s to t that travels along 
    # edges with flow = 1. 
    # I would suggest returning the parent dictionary
    # (see bfs in network_flow for starter code)
    pass

def unit_flow_path(f, s, t):
    # Uses bfs_unit_flow to find a path in f
    # from s to t with flow = 1 along each edge. 
    pass

def edge_disjoint_paths(G, s, t):
    # Compute a maximum number of edge disjoint paths from s to t. 
    # Recall that the reduction here is to create a capacity of 1
    # for each edge of G, then call network flow to compute a 
    # max flow. 
    # Then until there aren't any more such paths, find a unit flow
    # path, add it to the output, and reduce all the flow values along
    # the path to 0. 
    pass

def vertex_disjoint_paths(G, s, t):
    # Find vertex disjoint paths. Reduce this to edge disjoint paths
    # by creating an in and an out version for each vertex
    # with a single edge between them. 
    # I took each u in G and created (u, "in") and (u, "out") vertices
    # to create a graph to pass to edge_disjoint_paths. 
    pass

def main():
    # Read the input

    # Create an escape network and calculate the number
    # of disjoint paths. 
    
    # Print out the paths
    pass

if __name__ == '__main__':
    main()