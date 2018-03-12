# Programming Assignment 4
# Download the following text file (right click and select "Save As..."): SCC.txt
# The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the  row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646
# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.
#################################################################################################

# Kosaraju's algorithm to find the strongly connected components of a directed graph
# author: NL

from collections import defaultdict
 

class graph:
    def __init__(self, verNum):
        self.verNum = verNum
        self.graph = defaultdict(list)
        
    def addEdge(self, v, e):
        self.graph[v].append(e)
        
    def reverse(self):
        gRev = graph(self.verNum)
        for v in self.graph:
            for e in self.graph[v]:
                gRev.addEdge(e, v)
        return gRev
        
    # DFS for a single node + timing (for the 1st run)
    def DFS_timing(self, u, visited, stack):
        visited[u - 1] = True
        for v in self.graph[u]:
            if visited[v - 1] == False:
                self.DFS_timing(v, visited, stack)
        stack.append(u) # first finish, first in
    
    # DFS for a single node + find SCC 
    def DFS_SCC(self, u, visited, uscc):
        visited[u - 1] = True
        
        for v in self.graph[u]:
            if visited[v - 1] == False:
                self.DFS_SCC(v, visited, uscc)
        uscc.append(u)      
        
    # Kosaraju
    def Kosaraju(self):
        # run DFS + timing on the original graph
        visited = [False] * self.verNum
        stack = []
        for u in range(1, self.verNum + 1): 
            if visited[u - 1] == False:
                self.DFS_timing(u, visited, stack)
        print(stack)

        # run DFS on the reversed graph
        gre = self.reverse()
        visited = [False] * self.verNum
        scc = []
        while stack:
            u = stack.pop()
            if visited[u - 1] == False:
                uscc = []                
                gre.DFS_SCC(u, visited, uscc)
                scc.append(uscc)
        return scc
                