import sys

def tsp_dynamic_programming(distance_matrix):
    """Solve TSP using Dynamic Programming (Held-Karp Algorithm)."""
    n = len(distance_matrix)
    memo = {}

    def visit(city, visited_mask):
        """Recursively solve the TSP using dynamic programming and memoization."""
        if visited_mask == (1 << n) - 1:  # All cities visited
            return distance_matrix[city][0]  # Return to the start city

        if (city, visited_mask) in memo:
            return memo[(city, visited_mask)]

        min_distance = float('inf')
        for next_city in range(n):
            if not visited_mask & (1 << next_city):
                new_visited_mask = visited_mask | (1 << next_city)
                distance = distance_matrix[city][next_city] + visit(next_city, new_visited_mask)
                min_distance = min(min_distance, distance)

        memo[(city, visited_mask)] = min_distance
        return min_distance

    return visit(0, 1 << 0)  # Start from city 0
