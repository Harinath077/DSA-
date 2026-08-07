class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

  
        c = len(cuts)
        # adding boundaries
        arr = [0] + cuts + [n]
        arr.sort()
        dp = [[0] * (c  + 2) for _ in range(c + 2)]

        for i in range(c, 0, -1):
            for j in range(i, c+1):
                min_ = float('inf')

                for k in range(i, j+1):
                    cost = arr[j+1] - arr[i-1]
                    left = dp[i][k-1]
                    right = dp[k+1][j]
                    min_ = min( min_, 
                                cost + left + right)
                dp[i][j] = min_
                


        return dp[1][c]