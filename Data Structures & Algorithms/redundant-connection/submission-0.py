class Solution:
    def find(self, node, parent):
        if parent[node] == node:
            return node
        return self.find(parent[node], parent)

    def union(self, a, b, parent, rank):
        pa = self.find(a, parent)
        pb = self.find(b, parent)

        if pa != pb:
            if rank[pa] < rank[pb]:
                parent[pa] = pb
                rank[pb] += rank[pa]
            else:
                parent[pb] = pa
                rank[pa] += rank[pb]
        else:
            return [a, b]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]
        result = []

        for edge in edges:
            red_edge = self.union(edge[0], edge[1], parent, rank)
            if red_edge:
                result = red_edge
            
        return result