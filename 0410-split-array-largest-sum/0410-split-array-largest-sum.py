class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        def canSplit(sumLimit):
            currSum = 0
            subarrays = 1

            for num in nums:
                if num + currSum > sumLimit:
                    subarrays += 1
                    currSum  = num
                else:
                    currSum += num
            return subarrays <= k

        low = max(nums)
        high = sum(nums)

        while low <= high:

            mid = low + (high - low) // 2

            if canSplit(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low