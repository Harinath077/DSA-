class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        n = len(nums)
        middle = n // 2
        middle_elem = nums[middle]
        
        # if edage cases
        if( n == 1 ):
            return True
        return freq[middle_elem] == 1
            
        
        