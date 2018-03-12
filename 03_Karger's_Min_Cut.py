# Programming Assignment 3
# Download the following text file (right click and select "Save As..."): kargerMinCut.txt
# The file contains the adjacency list representation of a simple undirected graph. 
# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.
###################################################################################

# Karger's Min Cut algorithm
# author: NL

import copy as c
def contract(arr):
    """Karger's Min Cut algorithm: remove 1 edge at a time, 
    randomly choose two nodes,
    merging the 2 nodes that correspond to this edge, until we end up with 2 nodes.
    """

    #make a copy of the graph, so the original list is not changed
    copy = c.deepcopy(arr)

    while len(copy) > 2:
        #print(copy)
        # randomly choose a list l1 in copy; assign u = l1[0]
        l1 = copy[randint(0, len(copy) - 1)]
        #print(l1)
        u = l1[0]		
        # randomly choose another item in l1; assign v to this item
        v = l1[randint(1, len(l1) - 1)]
        #print(u, v)

        for x in copy:
            # find the list l2 in copy with the first time = v
            if x[0] == v:
                l2 = x
                #print(l2)
        # redirect any other edge originally pointing to v to u
        for x in copy:
            if x[0] in l2[1:] and x != l1:
                while v in x:
                    x.remove(v)
                    x.append(u)	

        # update l1
        while v in l1:
            l1.remove(v)
        l1.extend(l2[1:])
        while u in l1:
            l1.remove(u)
        l1.insert(0, u)
        
        copy.remove(l2)
        
    print(copy)
    
    return len(copy[0]) - 1
