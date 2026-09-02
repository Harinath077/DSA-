class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            queue = deque()
            queue.append( (r, c) )
            visited[r][c] = True
            while queue:
                x, y = queue.popleft()
                for dr, dc in directions:
                    nr = dr + x
                    nc = dc + y

                    if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == False and grid[nr][nc] == '1':
                        visited[nr][nc] = True
                        queue.append( (nr, nc) )
                        

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n) ]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islands = 0

        for r in range(n):
            for c in range(m):
                if visited[r][c] == False and grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands
