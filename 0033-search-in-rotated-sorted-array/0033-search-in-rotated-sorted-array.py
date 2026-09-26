class Solution:
    def search(self, nums: list[int], target: int) -> int:

        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1
        