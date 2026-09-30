class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        # edge case 
        if not nums:
            return 0

        longest = float('-inf')
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                while num + count in numSet:
                    count += 1
                longest = max(longest, count)

        return longest
