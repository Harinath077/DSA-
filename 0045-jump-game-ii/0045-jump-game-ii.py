class Solution:
    """  
    dfs(i) --> retun the minimum number of steps to reach last index from i
    """
    def jump(self, nums: List[int]) -> int:
        
        def dfs(index):

            if index >= n-1:
                return 0
            
            if memo[index] != -1:
                return memo[index]
            
            min_ = float('inf')
            jumps = nums[index]
            for j in range(1, jumps + 1):
                min_ = min( min_, 1 + dfs(index + j))

            memo[index] = min_
            return memo[index]
        
        n = len(nums)
        dp = [float('inf')] * n

        dp[n-1] = 0

        for index in range(n-2, -1, -1):
            min_ = float('inf')
            jumps = nums[index]
            for j in range(1, min(jumps, n - index - 1)+1):
                min_ = min( min_, 1 + dp[index + j])

            dp[index] = min_
            
        return dp[0]