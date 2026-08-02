class Solution:
    
    def isSubsetSum(self, nums: List[int], k : int) -> bool:
        
        n = len(nums)
        dp = [[False] * (k+1) for _ in range(n) ]

        for i in range(n):
            dp[i][0] = True
        
        if nums[0] <= k:
            dp[0][nums[0]] = True
        

        for index in range(1, n):
            for target in range(1, k+1):
                
                notTake = dp[index-1][target]
                take = False
                if( nums[index] <= target ):
                    take = dp[index-1][target - nums[index]]
                
                dp[index][target] = notTake or take
            

        return dp[n-1][k]

    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        # invalid case
        if totalSum & 1 != 0:
            return False
        
        return self.isSubsetSum(nums, totalSum // 2)
        