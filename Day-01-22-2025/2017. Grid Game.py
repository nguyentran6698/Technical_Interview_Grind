def gridGame(grid: list[list[int]]) -> int:
    n = len(grid[0])
    
    # Compute prefix sums for the bottom row
    prefix_bottom = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i - 1]
    
    # Compute suffix sums for the top row
    suffix_top = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_top[i] = suffix_top[i + 1] + grid[0][i]
    
    # Find the minimum of the maximum points the second robot can collect
    result = float('inf')
    for k in range(n):
        # Points available to the second robot if the first robot moves down at column k
        points = max(prefix_bottom[k], suffix_top[k + 1])
        result = min(result, points)
    
    return result

def gridGame(grid: list[list[int]]) -> int:
    n = len(grid[0])
    
    # DP arrays to store the maximum points the second robot can collect
    dp_top = [0] * (n + 1)
    dp_bottom = [0] * (n + 1)
    
    # Fill dp_bottom (prefix sums for the bottom row)
    for i in range(1, n + 1):
        dp_bottom[i] = dp_bottom[i - 1] + grid[1][i - 1]
    
    # Fill dp_top (suffix sums for the top row)
    for i in range(n - 1, -1, -1):
        dp_top[i] = dp_top[i + 1] + grid[0][i]
    
    # Find the minimum of the maximum points the second robot can collect
    result = float('inf')
    for k in range(n):
        points = max(dp_bottom[k], dp_top[k + 1])
        result = min(result, points)
    
    return result

def gridGame(grid: list[list[int]]) -> int:
    n = len(grid[0])
    
    # Compute total points in the top and bottom rows
    total_top = sum(grid[0])
    total_bottom = sum(grid[1])
    
    # Initialize variables to track the best path for the first robot
    result = float('inf')
    prefix_top = 0
    prefix_bottom = 0
    
    for k in range(n):
        # Points available to the second robot if the first robot moves down at column k
        points_top = total_top - prefix_top - grid[0][k]
        points_bottom = prefix_bottom
        points = max(points_top, points_bottom)
        
        # Update the result
        result = min(result, points)
        
        # Update prefix sums
        prefix_top += grid[0][k]
        prefix_bottom += grid[1][k]
    
    return result


def gridGame(grid: list[list[int]]) -> int:
    n = len(grid[0])
    
    # Compute prefix sums for the bottom row
    prefix_bottom = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i - 1]
    
    # Compute suffix sums for the top row
    suffix_top = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_top[i] = suffix_top[i + 1] + grid[0][i]
    
    # Binary search to find the minimum of the maximum points
    left = 0
    right = sum(grid[0]) + sum(grid[1])
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        is_possible = False
        
        # Check if mid is achievable
        for k in range(n):
            if prefix_bottom[k] <= mid and suffix_top[k + 1] <= mid:
                is_possible = True
                break
        
        if is_possible:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

def gridGame(grid: list[list[int]]) -> int:
    n = len(grid[0])
    
    # Compute total points in the top and bottom rows
    total_top = sum(grid[0])
    total_bottom = sum(grid[1])
    
    # Initialize variables to track the best path for the first robot
    result = float('inf')
    prefix_top = 0
    prefix_bottom = 0
    
    for k in range(n):
        # Points available to the second robot if the first robot moves down at column k
        points_top = total_top - prefix_top - grid[0][k]
        points_bottom = prefix_bottom
        points = max(points_top, points_bottom)
        
        # Update the result
        result = min(result, points)
        
        # Update prefix sums
        prefix_top += grid[0][k]
        prefix_bottom += grid[1][k]
    
    return result


# 1. Prefix and Suffix Sums
# Idea: Precompute prefix sums for the bottom row and suffix sums for the top row. For each possible path of the first robot (determined by the column where it moves down), calculate the maximum points the second robot can collect using the precomputed sums.

# Steps:

# Compute prefix sums for the bottom row.

# Compute suffix sums for the top row.

# For each possible column where the first robot moves down, calculate the maximum points the second robot can collect.

# Return the minimum of these maximum values.

# Time Complexity: O(n), where n is the number of columns.

# Space Complexity: O(n).

# 2. Dynamic Programming (DP)
# Idea: Use dynamic programming to track the optimal paths for both robots. Define DP states to represent the points collected by the first and second robots at each step.

# Steps:

# Define DP states for the first robot's path.

# Define DP states for the second robot's path based on the first robot's choices.

# Iterate through all possible paths and compute the result.

# Time Complexity: O(n).

# Space Complexity: O(n).

# 3. Greedy Approach
# Idea: The first robot should aim to minimize the maximum points available to the second robot. This can be achieved by greedily choosing the path that leaves the least valuable options for the second robot.

# Steps:

# For each possible column where the first robot moves down, calculate the points left for the second robot.

# Choose the path that minimizes the maximum points the second robot can collect.

# Time Complexity: O(n).

# Space Complexity: O(1).

# 4. Binary Search
# Idea: Use binary search to find the minimum possible maximum points the second robot can collect. Define a search space for the points and check if a given value is achievable.

# Steps:

# Define the search space (e.g., 0 to the total sum of points).

# Use binary search to find the minimum maximum points the second robot can collect.

# For each midpoint in the search, check if it is achievable by simulating the robots' paths.

# Time Complexity: O(n log S), where S is the total sum of points.

# Space Complexity: O(1).

# 5. Simulation
# Idea: Simulate all possible paths for the first robot and compute the points the second robot can collect for each path. Choose the path that minimizes the second robot's maximum points.

# Steps:

# Iterate through all possible columns where the first robot moves down.

# For each path, compute the points left for the second robot.

# Track the minimum of the maximum points the second robot can collect.

# Time Complexity: O(n).

# Space Complexity: O(1).

# Summary of Approaches
# Approach	Time Complexity	Space Complexity	Notes
# Prefix and Suffix Sums	O(n)	O(n)	Most efficient and straightforward.
# Dynamic Programming	O(n)	O(n)	Useful for understanding DP concepts.
# Greedy Approach	O(n)	O(1)	Intuitive but requires careful reasoning.
# Binary Search	O(n log S)	O(1)	Useful for problems with a search space.
# Simulation	O(n)	O(1)	Simple but less efficient for larger inputs.