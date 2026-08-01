# Using Tabulation
class Solution:
    def rob(self, arr: List[int]) -> int:
        # edge case
        if not arr: 
            return 0

        if len(arr) == 1:
                return arr[0]
                
        n = len(arr)
        index = 0

        # initialization
        prev2 = arr[0]
        prev1 = max(arr[0], arr[1])
        for i in range(2, n):
            take = arr[i] + prev2
            notTake = 0 + prev1
            curr = max(take, notTake)

            prev2 = prev1
            prev1 = curr

        return prev1


