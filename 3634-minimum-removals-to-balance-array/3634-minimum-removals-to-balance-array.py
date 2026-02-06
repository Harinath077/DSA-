class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        left = 0
        max_keep = 0

        for right in range(n):
            # Shrink window until balanced
            while nums[right] > nums[left] * k:
                left += 1

            # Update largest balanced window
            max_keep = max(max_keep, right - left + 1)

        # Minimum removals
        return n - max_keep