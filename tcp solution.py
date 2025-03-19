import sys  # Import sys module for handling large numbers

"""
Implementation: Implement the chosen method in a programming language of your choice. Document
your code with comments explaining key functions (e.g., state-space, recursion, bounding).
(c) Results: Output the final route and total distance. Share any intermediate results you find relevant.
"""

# Adjacency matrix representing the distances between cities
distances = [
    [0, 12, 10, 11, 7, 9, 12],  # Distances from city 1
    [12, 0, 8, sys.maxsize, sys.maxsize, sys.maxsize, 3],  # From city 2
    [10, 8, 0, 12, sys.maxsize, sys.maxsize, sys.maxsize],  # From city 3
    [11, sys.maxsize, 12, 0, 9, sys.maxsize, sys.maxsize],  # From city 4
    [7, sys.maxsize, sys.maxsize, 9, 0, 6, sys.maxsize],  # From city 5
    [9, sys.maxsize, sys.maxsize, sys.maxsize, 6, 0, 10],  # From city 6
    [12, 3, sys.maxsize, sys.maxsize, sys.maxsize, 10, 0]   # From city 7
]

num_cities = len(distances)  # Number of cities

def tsp_nearest_neighbor(start=0):
    """
    Implements the Nearest Neighbor algorithm for solving the Traveling Salesman Problem (TSP).
    - Selects the closest unvisited city at each step.
    - Returns the final route and total travel cost.
    """
    visited = [False] * num_cities  # Track visited cities
    path = [start]  # Start from the given city
    visited[start] = True  # Mark starting city as visited
    total_cost = 0  # Initialize total cost
    
    for _ in range(num_cities - 1):  # Loop to visit all cities
        last = path[-1]  # Get last visited city
        nearest_city = None  # Initialize nearest city
        min_distance = sys.maxsize  # Initialize minimum distance as large value
        
        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city] and distances[last][city] < min_distance:
                min_distance = distances[last][city]  # Update minimum distance
                nearest_city = city  # Update nearest city
        
        if nearest_city is not None:
            path.append(nearest_city)  # Add city to path
            visited[nearest_city] = True  # Mark city as visited
            total_cost += min_distance  # Update total cost
    
    total_cost += distances[path[-1]][start]  # Return to start city to complete the tour
    path.append(start)  # Add start city to complete cycle
    
    return path, total_cost  # Return final path and cost

# Solve the TSP using Nearest Neighbor
optimal_path, optimal_cost = tsp_nearest_neighbor()
print("Optimal Route:", optimal_path)  # Print the optimal path
print("Minimum Cost:", optimal_cost)  # Print the minimum cost
