class Solution:
    """ 
    tabulations
        dp[i][True]  = max alternating sum using nums[i:]
               when the next selected number gets +

        dp[i][False] = max alternating sum using nums[i:]
               when the next selected number gets -
        
        Let's use:

        column 0 → False
        column 1 → True

        So:

        dp[i][0]  # ops == False
        dp[i][1]  # ops == True
    """
    def maxAlternatingSum(self, nums: List[int]) -> int:

        n = len(nums)
        n = len(nums)

        dp = [[0, 0] for _ in range(n + 1)]

        for index in range(n - 1, -1, -1):

            for ops in [True, False]:

                notTake = dp[index + 1][ops]

                if ops == True:
                    take = nums[index] + dp[index + 1][not ops]
                else:
                    take = -nums[index] + dp[index + 1][not ops]

                dp[index][ops] = max(take, notTake)

        return dp[0][True]
