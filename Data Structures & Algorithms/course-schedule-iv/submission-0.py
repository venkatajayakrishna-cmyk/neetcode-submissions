class Solution:
    def bfs(self, adj, start, end):
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)

        while queue:
            course = queue.popleft()

            for prerequisite in adj.get(course, []):
                if prerequisite == end:
                    return True
                
                if prerequisite in visited:
                    continue
                
                visited.add(prerequisite)
                queue.append(prerequisite)
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for prerequisite in prerequisites:
            adj.setdefault(prerequisite[0], []).append(prerequisite[1])
        result = []
        for query in queries:
            result.append(self.bfs(adj, query[0], query[1]))
        return result