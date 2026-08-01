from functools import cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        @cache
        def dfs(i, j):
            # base cases
            if j < 0 or j >= n:
                return float('inf')

            if i == n-1:
                return matrix[i][j]

            if memo[i][j] != -1:
                return memo[i][j]

            below = matrix[i][j] + dfs(i + 1, j)
            dRight = matrix[i][j] + dfs(i + 1, j + 1)
            dLeft = matrix[i][j] + dfs(i + 1, j - 1)

            memo[i][j] = min( below, dRight, dLeft )

            return memo[i][j]
        
        n = len(matrix)
        min_ = float('inf')
        memo = [[-1] * n for _ in range(n)]

        for j in range(n):
            min_ = min( min_, dfs(0, j))
        
        return min_

