class Solution:
    """ 
    There are 2 possible ways to give the largest 3 sum
    1. 3 largest +ve gives the largest value
    2. 2 most negative nums , with maximum nums give largest value
    whyyy?
    --------> 2 -ve nums give +ve nums ( that is the logic)
    """
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        max1 = nums[-1]
        max2 = nums[-2]
        max3 = nums[-3]
        
        min1 = nums[0]
        min2 = nums[1]

        return max(
            max1 * max2 * max3,
            min1 * min2 * max1
        )