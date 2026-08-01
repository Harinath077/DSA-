class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]

        # base case

        dp[m-1][n-1] = 1

        for r in range(m):
            dp[r][n-1] = 1
        
        for c in range(n):
            dp[m-1][c] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
           
                down = dp[r+1][c] 
                right = dp[r][c+1] 
                dp[r][c] = down + right 

        return dp[0][0]
        