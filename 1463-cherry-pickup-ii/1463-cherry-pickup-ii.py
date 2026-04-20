class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def helper(i, j1, j2, dp):
            # Out of bounds
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')
            
            # Memoization check
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            
            # Last row
            if i == n-1:
                if j1 == j2:
                    dp[i][j1][j2] = grid[i][j1]
                else:
                    dp[i][j1][j2] = grid[i][j1] + grid[i][j2]
                return dp[i][j1][j2]
            
            # Move to next row
            max_ch = float('-inf')
            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    newj1 = j1 + dj1
                    newj2 = j2 + dj2
                    choc = helper(i+1, newj1, newj2, dp)
                    max_ch = max(max_ch, choc)
            
            if j1 == j2:
                dp[i][j1][j2] = max_ch + grid[i][j1]
            else:
                dp[i][j1][j2] = max_ch + grid[i][j1] + grid[i][j2]
            
            return dp[i][j1][j2]
        
        n = len(grid)
        m = len(grid[0])
        # Initialize DP array
        dp = [[[-1 for _ in range(m)] for __ in range(m)] for ___ in range(n)]
        
        return helper(0, 0, m-1, dp)