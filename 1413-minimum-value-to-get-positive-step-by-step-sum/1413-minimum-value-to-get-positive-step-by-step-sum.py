class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        currSum = 0
        minPrefixSum = 0

        for num in nums:
            currSum += num
            minPrefixSum = min( minPrefixSum, currSum)
        return 1 - minPrefixSum