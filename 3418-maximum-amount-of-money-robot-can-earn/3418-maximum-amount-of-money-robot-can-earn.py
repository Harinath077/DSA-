class Solution:
    def maximumAmount(self, coins):
        n, m = len(coins), len(coins[0])

        # dp[r][c][k] = max coins from (r,c) to end
        dp = [[[float('-inf')] * 3 for _ in range(m)] for _ in range(n)]

        # 🎯 Fill from bottom-right → top-left
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                for k in range(3):

                    val = coins[r][c]

                    # 🟢 Base case (destination)
                    if r == n - 1 and c == m - 1:
                        if val < 0 and k > 0:
                            dp[r][c][k] = 0
                        else:
                            dp[r][c][k] = val
                        continue

                    # next positions
                    down = dp[r+1][c][k] if r + 1 < n else float('-inf')
                    right = dp[r][c+1][k] if c + 1 < m else float('-inf')

                    # ✅ option 1: take value
                    take = val + max(down, right)

                    # ✅ option 2: neutralize
                    skip = float('-inf')
                    if val < 0 and k > 0:
                        down2 = dp[r+1][c][k-1] if r + 1 < n else float('-inf')
                        right2 = dp[r][c+1][k-1] if c + 1 < m else float('-inf')
                        skip = max(down2, right2)

                    dp[r][c][k] = max(take, skip)

        return dp[0][0][2]