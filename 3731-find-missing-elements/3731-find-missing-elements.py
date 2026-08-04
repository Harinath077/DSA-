class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_ = min(nums)
        max_ = max(nums)
        res = []

        for i in range(min_, max_ + 1):
            if i not in set(nums):
                res.append(i)
        return res