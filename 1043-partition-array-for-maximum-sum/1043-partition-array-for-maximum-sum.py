class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        def helper(i): # return the maxSum from i to n-1

            # base case 
            if i == n:
                return 0
            
            if memo[i] != -1:
                return memo[i]

            maxSum = float('-inf')
            maxAns = float('-inf')
            length = 0

            for j in range(i, min(i + k, n)):
                length += 1
                maxSum = max( arr[j], maxSum)
                totalSum = maxSum * length + helper(j + 1)
                maxAns = max( totalSum, maxAns)
            
            memo[i] = maxAns

            return memo[i]
        
        n = len(arr)
        memo = [-1] * n
        return helper(0)
