
from collections import defaultdict, deque
from typing import List
# Solution 1: DFS with State Tracking
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # States: 0 = unvisited, 1 = visiting, 2 = visited (safe)
        state = [0] * n
        result = []

        def is_safe(node):
            if state[node] == 1:
                # Cycle detected
                return False
            if state[node] == 2:
                # Already processed and safe
                return True
            
            # Mark as visiting
            state[node] = 1
            
            # Check all neighbors
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False
            
            # Mark as visited (safe)
            state[node] = 2
            return True

        for node in range(n):
            if is_safe(node):
                result.append(node)

        return result
# Solution 2: Topological Sort (Kahn's Algorithm)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # Reverse the graph
        reverse_graph = defaultdict(list)
        indegree = [0] * n

        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)
                indegree[i] += 1

        # Queue for nodes with 0 indegree (terminal nodes)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # Process nodes in topological order
        safe_nodes = []
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Sort the result
        safe_nodes.sort()
        return safe_nodes
# Solution 3: Iterative DFS with Stack
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # States: 0 = unvisited, 1 = visiting, 2 = visited (safe)
        state = [0] * n
        result = []

        for node in range(n):
            if state[node] != 0:
                continue
            
            stack = [(node, False)]  # (node, is_post_order)
            while stack:
                current, is_post_order = stack.pop()
                if is_post_order:
                    # Post-order: mark as visited (safe)
                    state[current] = 2
                    result.append(current)
                else:
                    if state[current] == 1:
                        # Cycle detected
                        break
                    if state[current] == 2:
                        # Already processed
                        continue
                    
                    # Mark as visiting
                    state[current] = 1
                    stack.append((current, True))  # Post-order marker
                    
                    # Push neighbors to stack
                    for neighbor in graph[current]:
                        stack.append((neighbor, False))
        
        # Sort the result
        result.sort()
        return result

# DFS with State Tracking: Simple and intuitive, but may cause stack overflow for very large graphs.

# Topological Sort: Efficient and avoids recursion, but requires building a reverse graph.

# Iterative DFS: Avoids recursion stack overflow and is efficient for large graphs.