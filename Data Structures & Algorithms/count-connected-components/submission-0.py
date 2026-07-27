class Solution:
    def find(self, node, parent):
        if parent[node] == node:
            return node
            
        return self.find(parent[node], parent)
    
    def union(self, a, b, parent, rank):
        p1 = self.find(a, parent)
        p2 = self.find(b, parent)

        if p1 != p2:
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        count = 0

        for edge in edges:
            self.union(edge[0], edge[1], parent, rank)

        for i in range(n):
            if parent[i] == i:
                count += 1

        return count
