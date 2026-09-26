class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target:
                return True
            # handling duplicate
            elif nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            # left is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right is sorted
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False