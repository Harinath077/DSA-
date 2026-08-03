class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        n = len(coins)
        prev = [0] * (amount + 1)

        # base case
        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = 1
        
        for index in range(1, n):
            curr = [0] * (amount + 1)
            for target in range(amount + 1):

                notTake = prev[target]
                take = 0
                if coins[index] <= target:
                    take = curr[target - coins[index]]
                
                curr[target] = take + notTake
            
            prev = curr

        return prev[amount]