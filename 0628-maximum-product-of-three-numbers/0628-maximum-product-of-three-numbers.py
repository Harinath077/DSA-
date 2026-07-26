class Solution:
    """ 
    There are 2 possible ways to give the largest 3 sum
    1. 3 largest +ve gives the largest value
    2. 2 most negative nums , with maximum nums give largest value
    whyyy?
    --------> 2 -ve nums give +ve nums ( that is the logic)
    """
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')

        min1 = float('inf')
        min2 = float('inf')

        for num in nums:

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            
            # negative handling
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(
            max1 * max2 * max3,
            min1 * min2 * max1
        )