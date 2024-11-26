# Traveling Salesman Problem (TSP) in Network Routing

## Project Overview
This project focuses on solving the **Traveling Salesman Problem (TSP)**, a classic **NP-complete problem**, using two optimization techniques:

1. **Greedy Algorithm**: An approximation method that solves TSP by iteratively selecting the nearest unvisited city.
2. **Dynamic Programming (Held-Karp Algorithm)**: An exact method for solving TSP efficiently using memoization and bitmasking, reducing the time complexity compared to brute force.

The project applies these algorithms to model **network routing**, where cities (or routers) are connected by paths with varying costs (distances). The goal is to optimize the path taken by a network router, visiting all nodes and returning to the starting point, minimizing the total cost (distance).

## Problem Domain
- **Networking / Optimization**
- **NP-complete Problems**
- **Routing Algorithms**

## Algorithms Implemented
1. **Greedy Algorithm**:
   - Starts at a random city and iteratively visits the nearest unvisited city.
   - Does not guarantee the optimal solution but provides a reasonable approximation in polynomial time.

2. **Dynamic Programming (Held-Karp Algorithm)**:
   - Uses dynamic programming to solve TSP more efficiently.
   - Reduces the time complexity from O(n!) to O(n^2 * 2^n), making it feasible for larger networks.
   - The algorithm uses bitmasking to represent visited cities and memoization to store intermediate results.

## Files and Directories
- **`tsp_greedy.py`**: Implements the Greedy Algorithm to solve TSP.
- **`tsp_dynamic_programming.py`**: Implements the Held-Karp Algorithm using Dynamic Programming.
- **`main.py`**: Runs the Greedy and Dynamic Programming algorithms, tests them on a randomly generated distance matrix, and prints the results.
- **`README.md`**: Project description, setup, and instructions.

## Installation
To run the project, you will need Python installed on your system. Additionally, the `numpy` library is required for matrix manipulation.

1. Clone the repository:
   ```bash
   git clone https://github.com/subhan-liaqat/tsp-network-routing.git
   cd tsp-network-routing
   ```
2. Install the required dependencies:
  ```bash
  pip install numpy
  ```

## Usage
Running the Project
1. Generate a random network (cities/routers) distance matrix.
2. Apply the Greedy Algorithm and Dynamic Programming (Held-Karp Algorithm) to find the optimal route.
3. The result includes the best route found by each algorithm and its corresponding total distance.
