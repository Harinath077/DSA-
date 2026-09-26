class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
       
        def helper(index, kLeft):

            # base case
            if kLeft == 1:
                return sum(nums[index : ])

            if dp[index][kLeft] != -1:
                return dp[index][kLeft]

            mini = float('inf')
            maxSum = float('-inf')

            for j in range(index, n-kLeft + 1):
                currSum = sum(nums[index : j+1])
                maxSum = max( currSum, helper(j + 1, kLeft - 1))
                mini = min(mini, maxSum)
            
            dp[index][kLeft] = mini
            return mini

        n = len(nums)
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]

        # base case
        for index in range(n):
            dp[index][1] = sum( nums[index:] )

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