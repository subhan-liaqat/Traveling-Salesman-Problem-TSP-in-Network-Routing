def calculate_distance(route, distance_matrix):
    """Calculate the total distance for a given route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to the start
    return total_distance

def tsp_greedy(distance_matrix):
    """Solve TSP using a Greedy Algorithm."""
    n = len(distance_matrix)
    visited = [False] * n
    route = [0]  # Start at the first city
    visited[0] = True
    current_city = 0
    
    for _ in range(n - 1):
        nearest_city = None
        min_distance = float('inf')
        
        for city in range(n):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                nearest_city = city
                min_distance = distance_matrix[current_city][city]
        
        route.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city
    
    return route, calculate_distance(route, distance_matrix)
