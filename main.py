import numpy as np
from tsp_greedy import tsp_greedy
from tsp_dynamic_programming import tsp_dynamic_programming

def generate_distance_matrix(n):
    """Generate a random distance matrix for the network (cities/routers)."""
    matrix = np.random.randint(1, 100, size=(n, n))
    np.fill_diagonal(matrix, 0)  # No distance to itself
    return matrix

def print_route(route, distance):
    """Print the TSP route and its total distance."""
    print(f"Route: {route}")
    print(f"Total Distance: {distance}")

def main():
    # Set up a network of 5 cities/routers
    n = 5  # You can increase this number for larger networks
    distance_matrix = generate_distance_matrix(n)

    print("Greedy Algorithm Solution:")
    route, distance = tsp_greedy(distance_matrix)
    print_route(route, distance)

    print("\nDynamic Programming (Held-Karp) Solution:")
    distance = tsp_dynamic_programming(distance_matrix)
    print(f"Minimum Distance: {distance}")

if __name__ == "__main__":
    main()
