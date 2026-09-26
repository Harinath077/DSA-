class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
       
        n = len(nums)
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]

        # base case
        currSum = 0
        for index in range(n-1, -1, -1):
            currSum += nums[index]
            dp[index][1] = currSum

        for index in range(n-1, -1, -1):
            for kLeft in range(2, k+1):

                mini = float('inf')
                currSum = 0

                for j in range(index, n-kLeft + 1):
                    currSum += nums[j]
                    largest = max( currSum, dp[j + 1][kLeft - 1])
                    mini = min(mini, largest)
                
                dp[index][kLeft] = mini
            
        return dp[0][k]