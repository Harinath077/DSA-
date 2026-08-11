class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        dp = [[-1] * (k+1) for _ in range(n)]

        # base case
        currSum = 0
        for i in range(n-1, -1, -1):
            currSum += nums[i]
            dp[i][1] = currSum / (n - i) 
        
        for kLeft in range(2, k+1):
            for i in range(n-1, -1, -1):
            
                # these are variable like global ( initialized for each functions calls )
                currSum = 0
                maxAns = 0

                for j in range(i, n - kLeft+1):
                    currSum += nums[j]
                    totalSum = currSum / (j - i + 1) + dp[j+1][kLeft - 1]
                    maxAns = max( totalSum, maxAns)
                dp[i][kLeft] = maxAns
                
        return dp[0][k]