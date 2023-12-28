from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjacency = {i: [] for i in range(n)}
        # Treat the graph like an undirected graph
        for a, b in connections:
            adjacency[a].append((b, 1))  # Direction 1 represents the original direction
            adjacency[b].append((a, 0))  # Direction 0 represents the reversed direction

       
        def dfs(city, visited):
            visited.add(city)
            count = 0

            for neighbor, direction in adjacency[city]:
                if neighbor not in visited:
                    count += direction  # Increment count based on the direction of the edge
                    count += dfs(neighbor, visited)

            return count

        visited = set()
        return dfs(0, visited)

