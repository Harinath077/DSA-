class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            visited[r][c] = True

            for dr, dc in dir:
                nr, nc = dr + r, dc + c
                if( 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and not visited[nr][nc] ):
                    visited[nr][nc] = True
                    dfs(nr, nc)

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        islands = 0

        dir = [(0,-1),(-1, 0),(0, 1),(1, 0)]

        for r in range(n):
            for c in range(m):
                if( not visited[r][c] and grid[r][c] == '1' ):
                    islands += 1
                    dfs(r, c)
        return islands
                