class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        freq = {}

        for num in nums:
            if num in freq:
                return True
            freq[num] = freq.get(num, 0) + 1
        return False
