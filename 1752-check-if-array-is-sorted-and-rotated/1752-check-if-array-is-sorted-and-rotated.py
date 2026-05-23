class Solution:
    """
    The REAL Pattern

    A valid sorted-rotated array has:

    0 drops → already sorted
    1 drop → rotated sorted
    more than 1 drop → impossible

    """
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        count = 0
        for i in range(n):
            if( nums[i] > nums[(i+1) % n] ):
                count += 1
        
        return count <= 1
        