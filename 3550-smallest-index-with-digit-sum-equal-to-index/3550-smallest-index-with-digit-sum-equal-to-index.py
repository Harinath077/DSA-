class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def isEqual(num, index):
            sum_ = 0
            while num > 0:
                digit = num % 10
                sum_ += digit
                if sum_ > index:
                    return False
                num //= 10
            return True if sum_ == index else False
            
        for index, num in enumerate(nums):
            if isEqual(num, index):
                return index
        return -1

