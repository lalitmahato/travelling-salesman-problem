from itertools import permutations

# Distance matrix (rows and columns: A, B, C, D, E, F)
distances_between_cities = [
  #  A   B   C   D   E   F
    [0, 10, 15, 20, 25, 30],  # A
    [10, 0, 35, 25, 17, 28],  # B
    [15, 35, 0, 30, 28, 40],  # C
    [20, 25, 30, 0, 22, 16],  # D
    [25, 17, 28, 22, 0, 35],  # E
    [30, 28, 40, 16, 35, 0]   # F
]

# City labels for output
cities = ['A', 'B', 'C', 'D', 'E', 'F']

# Function to calculate the total distance of a route
def calculate_distance(route):
    total = 0
    # Add distance from first city (ie. A) to permatation first city
    total += distances_between_cities[0][cities.index(route[0])]
    # Add distances between permation cities in the route
    for i in range(len(route) - 1):
        total += distances_between_cities[cities.index(route[i])][cities.index(route[i + 1])]
    # Add distance from last city to starting city ie. A
    total += distances_between_cities[cities.index(route[-1])][0]
    return total

other_cities = cities[1:] # excluding starting city ie. A
min_distance = float('inf')
best_route = None

# Iterate through all permutations
for perm in permutations(other_cities):
    current_distance = calculate_distance(perm)
    if current_distance < min_distance:
        min_distance = current_distance
        best_route = perm

# Format the route to include starting and ending at A
full_route = ['A'] + list(best_route) + ['A']

# Print the result
print("Shortest route:", " -> ".join(full_route))
print("Total distance:", min_distance, "kilometers")
