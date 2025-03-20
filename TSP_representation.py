#Adjacency list representation.
graph = {
    1: [(2, 12), (3, 10), (7, 12)], #City 1 connects to city 2, 3 and 7 by 12, 10 and 12 distances respectively.
    2: [(1, 12), (3, 8), (4, 12)], #city 2 connects to city 1, 3 and 4 by 12, 8, and 12 distances respectively
    3: [(1, 10), (2, 8), (4, 11), (5, 3), (7, 9)], #city 3 connects to city 1,2,4,5 and 7 by distances 10, 8, 11,3, and 9 respectively.
    4: [(2, 12), (3, 11), (5, 11), (6, 10)], #city 4 connects to city 2, 3, 5, and 6 by distances 12, 11, 11, and 10 respectively.
    5: [(3, 3), (4, 11), (6, 6), (7, 7)], #city 5 connects to city 3, 4, 6 and 7 by distances 3, 11, 6 and 7 respectively
    6: [(4, 10), (5, 6), (7, 9)], #city 6 connects to city 4, 5, and 7 by distances 10, 6, and 9.
    7: [(1, 12), (3, 9), (5, 7), (6, 9)] #city 7 connects to city 1, 3, 5 and 6 by distances 12, 9, 7 and 9.
}

#Reason:
#Memory efficiency, this is because the graph for the Traveling Salesman Problem(TSP)contains only edges between directly connected cities hence it's sparse. An adjacency list only stores connections that exist rather than an exhaustive grid of all possible connections, saving memory compared to other presentations like adjacency matrix.
#Faster lookups for neighbors. With adjacency list, cities connected to a specific node can be quickly identified which streamlines the process of selecting paths during the algorithm's execution.