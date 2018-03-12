# Programming Assignment 5
# In this programming problem you'll code up Dijkstra's shortest-path algorithm.
# Download the following text file (Right click and select "Save As..."): dijkstraData.txt
# The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. 
# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. 
###############################################################################################

# Brute force implementation of Dijkstra' algorithm (a better way would be to use heap)
# author: NL

def dijkstra(source, edges):
    """compute the shortest path from the source to any other vertices
    edges = {node:[(tail, length)]}
    """
    shortest_path = {}
    visited = set() # seen vertices
    
    visited.add(source)
    shortest_path[source] = 0 # set the shortest distance from the source to itself = 0
    
    vertices = edges.keys() # total vertices
    while set(vertices - visited):
        min_dist = 1000000
        new_node = 0
        for u in visited:
            for v, length_uv in edges[u]:
                if v in visited:
                    continue
                if shortest_path[u] + length_uv < min_dist:
                    min_dist = shortest_path[u] + length_uv
                    new_node = v
        if new_node != 0:
            shortest_path[new_node] = min_dist
            visited.add(new_node)
    return shortest_path
        