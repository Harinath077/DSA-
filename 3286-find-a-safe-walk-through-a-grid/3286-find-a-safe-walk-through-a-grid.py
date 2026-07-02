class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])

        best = [[-1] * m for _ in range(n)]

        def dfs(i, j, hp):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            hp -= grid[i][j]

            if hp <= 0:
                return False

            if i == n - 1 and j == m - 1:
                return True

            if best[i][j] >= hp:
                return False

            best[i][j] = hp

            return (
                dfs(i + 1, j, hp) or
                dfs(i - 1, j, hp) or
                dfs(i, j + 1, hp) or
                dfs(i, j - 1, hp)
            )

        return dfs(0, 0, health)