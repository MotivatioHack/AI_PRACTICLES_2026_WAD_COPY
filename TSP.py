# Cost matrix representing distances between cities
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Total number of cities
n = len(cost)

# Start from city 0
visited = [0]

# Variable to store total travel cost
total = 0


# Repeat until all cities are visited
while len(visited) < n:

    # Current city = last visited city
    city = visited[-1]

    # Find nearest unvisited city using heuristic search
    nxt = min(
        (cost[city][i], i)
        for i in range(n)
        if i not in visited
    )

    # Add travel cost
    total += nxt[0]

    # Mark next city as visited
    visited.append(nxt[1])


# Return to starting city (city 0)
total += cost[visited[-1]][0]
visited.append(0)


# Print final path and minimum cost
print("Path:", visited)
print("Minimum Cost:", total)
