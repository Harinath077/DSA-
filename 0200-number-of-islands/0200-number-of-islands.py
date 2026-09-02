class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            visited[r][c] = True

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == False and grid[nr][nc] == '1':
                    dfs(nr, nc)

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n) ]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islands = 0

        for r in range(n):
            for c in range(m):
                if visited[r][c] == False and grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
