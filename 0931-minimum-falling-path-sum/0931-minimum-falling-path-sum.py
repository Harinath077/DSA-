class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        dp = [[0] * n for _ in range(n)]

        # base case
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]
        
        for i in range(n - 2, -1, -1):
            for j in range(n):
                below = matrix[i][j] + dp[i + 1][j]
                dRight = matrix[i][j] + dp[i + 1][j + 1] if j < n-1 else float('inf')
                dLeft = matrix[i][j] + dp[i + 1][j - 1] if j > 0 else float('inf')

                dp[i][j] = min(below, dRight, dLeft)

        return min(dp[0])




