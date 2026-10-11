class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfSquare = 0
        for index, num in enumerate(nums, 1):
            if n % index == 0:
                sumOfSquare += num * num
        return sumOfSquare