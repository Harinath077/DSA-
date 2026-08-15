class Solution:
    """  
    Case 1: All elements are 0 ---> return 0
    Case 2: The total XOR sum is non-zero ----> so longest one Arrays total length itself So return n
    Case 3: The total XOR sum is zero ----> means that xor is cancel outed the all element so removing one element will help in not cancle out the all element So return n-1
    """
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        # case 1
        if all(num == 0 for num in nums):
            return 0
        
        # compute totalXor 
        totalXor = 0
        for num in nums:
            totalXor ^= num
        
        # case 2

        if totalXor > 0:
            return n
        
        # case 3
        return n-1