from typing import List

class Solution:
    def rob(self, houses: List[int]) -> int:
        def max_value(arr: List[int]) -> int:
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            
            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])
            
            for i in range(2, len(arr)):
                curr = max(arr[i] + prev2, prev1)
                prev2, prev1 = prev1, curr
            
            return prev1

        n = len(houses)
        if n == 0:
            return 0
        if n == 1:
            return houses[0]

        # Exclude first house or last house
        exclude_first = houses[1:]
        exclude_last = houses[:-1]
        
        return max(max_value(exclude_first), max_value(exclude_last))
