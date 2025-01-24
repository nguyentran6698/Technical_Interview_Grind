# Solution 1: Rows and Cols Count
from typing import List


def countServers(grid:List[[int]]): # type: ignore
    m , n = len(grid) , len(grid[0]) if grid else 0
    results = 0
    rows = [sum(row) for row in grid]
    cols = [0] * n
    
    for j in range(n):
        for i in range(m):
            cols[j] += grid[i][j]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] and (rows[i] > 1 or cols[i] > 1):
                results += 1
    
    return results

def countServers(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0]) if grid else 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    result = 0

    def dfs(i, j):
        nonlocal count
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True
        count += 1
        # Explore the entire row and column
        for x in range(m):
            dfs(x, j)
        for y in range(n):
            dfs(i, y)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                count = 0
                dfs(i, j)
                if count > 1:
                    result += count
    return result


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

def countServers(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0]) if grid else 0
    uf = UnionFind(m * n)
    servers = []

    # Assign unique IDs to servers
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                servers.append((i, j))

    # Union servers in the same row
    row_map = {}
    for idx, (i, j) in enumerate(servers):
        if i in row_map:
            uf.union(row_map[i], idx)
        else:
            row_map[i] = idx

    # Union servers in the same column
    col_map = {}
    for idx, (i, j) in enumerate(servers):
        if j in col_map:
            uf.union(col_map[j], idx)
        else:
            col_map[j] = idx

    # Count servers in components with size > 1
    result = 0
    for idx in range(len(servers)):
        if uf.size[uf.find(idx)] > 1:
            result += 1
    return result

# 1. Using Union-Find (Disjoint Set Union - DSU)
# Idea: Treat each server as a node in a graph. Connect servers in the same row or column into the same connected component. At the end, count the number of servers that belong to components with more than one server.

# Steps:

# Assign a unique ID to each server.

# Use Union-Find to connect servers in the same row and same column.

# After processing all servers, count the number of servers in components with size > 1.

# Complexity: O(m * n * α(m * n)), where α is the inverse Ackermann function (very small, nearly constant).

# 2. Using Graph Traversal (DFS or BFS)
# Idea: Treat the grid as a graph where servers are nodes, and edges exist between servers in the same row or column. Use DFS or BFS to traverse connected components and count servers in components with more than one server.

# Steps:

# Iterate through the grid and identify all servers.

# For each server, perform DFS/BFS to explore all servers in the same row and column.

# If a component has more than one server, count all servers in that component.

# Complexity: O(m * n), as each server is visited once.

# 3. Using Row and Column Hashing
# Idea: Use dictionaries to track servers in each row and column. For each server, check if its row or column has more than one server.

# Steps:

# Create two dictionaries: one for rows and one for columns.

# Populate the dictionaries with the count of servers in each row and column.

# Iterate through the grid and count servers that are in a row or column with more than one server.

# Complexity: O(m * n).

# 4. Using Bitmasking
# Idea: Represent rows and columns as bitmasks. For each server, check if its row or column has more than one server using bitwise operations.

# Steps:

# Create two arrays: one for rows and one for columns, initialized to 0.

# For each server, set the corresponding bit in the row and column arrays.

# Iterate through the grid and count servers where the row or column has more than one server.

# Complexity: O(m * n).

# 5. Using Row and Column Pointers
# Idea: For each server, scan its entire row and column to check if there is another server.

# Steps:

# Iterate through the grid to identify all servers.

# For each server, scan its row and column to check for other servers.

# If another server is found, count the current server.

# Complexity: O(m * n * (m + n)), as for each server, we scan its row and column.


# Approach	Time Complexity	Space Complexity	Notes
# Row and Column Counts	O(m * n)	O(m + n)	Simple and efficient.
# Union-Find (DSU)	O(m * n * α(m * n))	O(m * n)	Useful for more complex connectivity problems.
# Graph Traversal (DFS)	O(m * n)	O(m * n)	Intuitive but requires more space for recursion/queue.
# Row and Column Hashing	O(m * n)	O(m + n)	Similar to the first approach but uses dictionaries.
# Bitmasking	O(m * n)	O(m + n)	Efficient but less intuitive.
# Row and Column Pointers	O(m * n * (m + n))	O(1)	Inefficient for large grids due to repeated scans.
