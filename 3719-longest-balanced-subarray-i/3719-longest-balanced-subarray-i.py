class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 0
        for i in range(n):
            evens = set()
            odds = set()
            for j in range(i, n):
                num = nums[j]
                if num % 2 == 0:
                    evens.add(num)
                else:
                    odds.add(num)
                if len(evens) == len(odds):
                    maxLen = max(j - i + 1, maxLen)
        return maxLen