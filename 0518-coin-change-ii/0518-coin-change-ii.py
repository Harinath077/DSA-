class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]

        # base case
        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = 1
        
        for index in range(1, n):
            for target in range(amount + 1):

                notTake = dp[index - 1][target]
                take = 0
                if coins[index] <= target:
                    take = dp[index][target - coins[index]]
                
                dp[index][target] = take + notTake

        return dp[n-1][amount]