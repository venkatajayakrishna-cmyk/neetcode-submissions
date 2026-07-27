from collections import deque

class Solution:
    def bfs(self, n, adj, start):
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        parent = [-1 for _ in range(n)]

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
                
                elif parent[node] != neighbor:
                    return False
            
        return len(visited) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for edge in edges:
            adj.setdefault(edge[0], []).append(edge[1])
            adj.setdefault(edge[1], []).append(edge[0])
        
        if adj:
            return self.bfs(n, adj, next(iter(adj)))
        else:
            return True