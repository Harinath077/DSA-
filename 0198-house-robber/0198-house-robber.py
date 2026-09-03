class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        # edge case 
        if n <= 1:
            return max(nums)   
             
        dp = [-1] * n

        # base case 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for index in range(2, n):
            take = nums[index] + dp[index - 2]
            notTake = dp[index - 1]

            dp[index] = max(take, notTake)
        
        return dp[n-1]