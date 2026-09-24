import bisect
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def lowerSearch(nums, target):
            low = 0
            high = n-1
            ans = n
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        def upperSearch(nums, target):
            low = 0
            high = n-1
            ans = n
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        n = len(nums) 
        lower = lowerSearch(nums, target)
        upper = upperSearch(nums, target)
        if lower == upper:
            return [-1, -1]
        return [lower, upper-1]