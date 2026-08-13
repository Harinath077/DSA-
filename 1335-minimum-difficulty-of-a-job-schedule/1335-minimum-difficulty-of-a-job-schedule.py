class Solution:
    """  
    partition approach : front partition 
    """
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)

        # edge case
        if n < d:
            return -1

        dp = [[float('inf')] * (d+1) for _ in range(n+1)]

        # base case 
        max_ = 0
        for index in range(n-1, -1, -1):
            max_ = max( max_, jobDifficulty[index])
            dp[index][1] = max_
        
        for balanceCuts in range(2, d+1):
            for index in range( n-1, -1, -1):
                
                maxElement = -1
                min_ = float('inf')

                for j in range(index, n):

                    maxElement = max( jobDifficulty[j], maxElement )
                    ans = maxElement + dp[j + 1][balanceCuts-1]
                    min_ = min(ans, min_)

                dp[index][balanceCuts] = min_
        
        return dp[0][d]
