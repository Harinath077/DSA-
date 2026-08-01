class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]

        # base case

        dp[m-1][n-1] = 1

        # last col
        for r in range(m):
            dp[r][n-1] = 1
        
        # last row
        for c in range(n):
            dp[m-1][c] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
           
                down = dp[r+1][c] 
                right = dp[r][c+1] 
                dp[r][c] = down + right 

        return dp[0][0]

"""
DP Definition:
--------------
dp[r][c] represents the number of unique paths from cell (r, c)
to the destination (m-1, n-1).

Why initialize the last row and last column with 1?
---------------------------------------------------
The robot can only move RIGHT or DOWN.

1. Last Row:
   Once the robot reaches the last row, it cannot move DOWN anymore.
   The only possible move is to keep moving RIGHT until the destination.
   Therefore, every cell in the last row has exactly ONE unique path.

       1 → 1 → 1

2. Last Column:
   Once the robot reaches the last column, it cannot move RIGHT anymore.
   The only possible move is to keep moving DOWN until the destination.
   Therefore, every cell in the last column has exactly ONE unique path.

       1
       ↓
       1
       ↓
       1

Initial DP table for a 3x3 grid:

    0 0 1
    0 0 1
    1 1 1

Transition:
-----------
For every other cell, the robot has two choices:
1. Move DOWN
2. Move RIGHT

Hence,

dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

We fill the table from bottom-right to top-left so that
the required states (down and right) are already computed.
"""
        