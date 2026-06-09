class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nums.sort()
        return (nums[-1] - nums[0]) * k