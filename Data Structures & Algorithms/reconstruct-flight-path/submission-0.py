class Solution:
    def dfs(self, adj, node, result):
        while adj.get(node, []):
            neighbor = adj[node].pop()

            self.dfs(adj, neighbor, result)
        result.append(node)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        start = "JFK"

        for ticket in tickets:
            adj.setdefault(ticket[0], []).append(ticket[1])
        
        for node in adj:
            adj[node] = sorted(adj[node], reverse=True)

        result = []
        self.dfs(adj, start, result)

        result.reverse()
        return result