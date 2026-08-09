class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        #  dp[i] = answer for the entire suffix arr[i...n-1]
        n = len(arr)
        dp = [0] * (n+1)

        # base case 
        dp[n] = 0

        for i in range(n-1, -1, -1):
            maxElement = float('-inf')
            maxAns = float('-inf')
            length = 0

            for j in range(i, min(i + k, n)):
                length += 1

                maxElement = max( arr[j], maxElement)

                totalSum = maxElement * length + dp[j + 1]
                maxAns = max( totalSum, maxAns)
            
            dp[i] = maxAns

    
        return dp[0]
          
            
        
        
