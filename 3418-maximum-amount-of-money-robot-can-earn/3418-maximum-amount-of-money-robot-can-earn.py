class Solution:
    def maximumAmount(self, coins):
        n, m = len(coins), len(coins[0])

        dp = [[[float('-inf')] * 3 for _ in range(m)] for _ in range(n)]

        # initialize start
        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                dp[0][0][k] = 0
            else:
                dp[0][0][k] = coins[0][0]

        for r in range(n):
            for c in range(m):
                for k in range(3):
                    if r == 0 and c == 0:
                        continue

                    val = coins[r][c]

                    # from top
                    if r > 0:
                        # take value
                        dp[r][c][k] = max(dp[r][c][k],
                                          dp[r-1][c][k] + val)
                        # neutralize
                        if val < 0 and k > 0:
                            dp[r][c][k] = max(dp[r][c][k],
                                              dp[r-1][c][k-1])

                    # from left
                    if c > 0:
                        dp[r][c][k] = max(dp[r][c][k],
                                          dp[r][c-1][k] + val)
                        if val < 0 and k > 0:
                            dp[r][c][k] = max(dp[r][c][k],
                                              dp[r][c-1][k-1])

        return max(dp[n-1][m-1])