class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # scan for rotten orange
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append( (i, j) )
        
        # queue processing multi source + level by level
        minutes = 0

        while queue:
            size = len(queue)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < n and 0 <= nc <m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append( (nr, nc))
        
            # after one complete bfs()
            if queue:
                minutes += 1

        # final scan for any fresh orange in grid
        for row in grid:
            if 1 in row:
                return -1
        return minutes

                
