
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        prev = [float('inf')] * (amount + 1)

        # base case : if only one coin
        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = target // coins[0]
            else:
                prev[target] = float('inf')

        for index in range(1, n):
            curr = [float('inf')] * (amount + 1)
            
            for target in range( amount + 1 ):

                notTake = prev[target]
                take = float('inf')
                
                if coins[index] <= target:
                    take = 1 + curr[target - coins[index]]
                
                curr[target] = min( take, notTake)
            
            prev = curr

        minCoins = prev[amount]

        if minCoins == float('inf'):
            return -1
        return minCoins
