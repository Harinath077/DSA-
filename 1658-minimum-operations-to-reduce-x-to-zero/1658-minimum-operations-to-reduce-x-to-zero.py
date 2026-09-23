class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        subArraySum = sum(nums) - x

        # edge case 
        if subArraySum < 0:
            return -1
        # return entier array
        if subArraySum == 0:
            return n

        left = 0
        right = 0
        longest = 0

        sum_ = 0

        while right < n:

            sum_ += nums[right]

            while sum_ > subArraySum:
                sum_ -= nums[left]
                left += 1
            
            if sum_ == subArraySum:
                longest = max(longest, right - left + 1)
            
            right += 1
        
        return n - longest if longest != 0 else -1
