from collections import deque

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    n = 0
    m = 0
    land = 2**31 - 1

    def bfs(self, grid, queue):
        visited = {}
        level = 0
        while queue:
            size = len(queue)

            for _ in range(size):
                cell = queue.popleft()

                for k in range(4):
                    ii = cell[0] + Solution.dx[k]
                    jj = cell[1] + Solution.dy[k]

                    if (ii < 0 or jj < 0 or
                        ii >= Solution.n or jj >= Solution.m or
                        grid[ii][jj] != Solution.land or
                        (ii, jj) in visited):
                        continue
                    
                    visited[(ii, jj)] = level + 1
                    queue.append((ii, jj))
            level += 1

        return visited

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        Solution.n = len(grid)
        Solution.m = len(grid[0])
        for i in range(Solution.n):
            for j in range(Solution.m):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        dist = self.bfs(grid, queue)
        for cell in dist.keys():
            grid[cell[0]][cell[1]] = dist[cell]
