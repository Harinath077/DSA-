class Solution:
    """  
    The Greedy thing is:
    The memoment the current Journey ( currGas < 0) fails, immediately dicard all strting positions involved [ Start --> i ] ( instead of going back and trying with diff starting instead of failed ones).
    
    Choosing the next ( i + 1 ) as the starting as the next candidate make the greedy thing here
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
            
        n = len(gas)
        currGas = 0
        start = 0

        for i in range(n):

            currGas += ( gas[i] - cost[i] )

            # Greedy decision
            if currGas < 0:
                start = i + 1
                currGas = 0
            
        return start

        