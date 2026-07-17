class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            queue = deque()
            queue.append( (r, c) )
            visited[r][c] = True

            while( queue ):
                x, y = queue.popleft()
                for dr, dc in dir:
                    nr, nc = dr + x, dc + y
                    if( 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc] ):
                        visited[nr][nc] = True
                        queue.append( (nr, nc))
                        bfs(nr, nc)

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        islands = 0

        dir = [(0,-1),(-1, 0),(0, 1),(1, 0)]

        for r in range(n):
            for c in range(m):
                if( not visited[r][c] and grid[r][c] == '1' ):
                    islands += 1
                    bfs(r, c)
        return islands
                