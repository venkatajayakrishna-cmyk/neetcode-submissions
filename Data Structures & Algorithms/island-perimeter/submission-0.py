class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, -1, 0, 1]
    
    def find_start(self, grid):
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    return (i, j)

    def bfs(self, grid, start):
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        perimeter = 0

        while queue:
            i, j = queue.popleft()

            perimeter += 4

            for k in range(4):
                ii = i + self.dx[k]
                jj = j + self.dy[k]

                if (ii < 0 or jj < 0 or
                    ii >= self.n or jj >= self.m):
                    continue
                
                if grid[ii][jj] == 1:
                    perimeter -= 1
                    if (ii, jj) not in visited:
                        queue.append((ii, jj))
                        visited.add((ii, jj))

        return perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        return self.bfs(grid, self.find_start(grid))