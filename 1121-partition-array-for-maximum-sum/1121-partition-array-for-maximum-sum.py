class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        

        n = len(arr)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            maxSum = 0
            currMax = 0
            for length in range(1, min(k, n-i)+1):
                
                
                currMax = max(currMax, arr[i+length - 1])
                currSum = (currMax * length) + dp[i + length]
                maxSum = max( maxSum, currSum)

            dp[i] = maxSum
        return dp[0]
