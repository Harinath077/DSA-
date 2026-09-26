class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        for index, num in enumerate(nums):
            if num == target:
                return True
        return False
