class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        # edge cases
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1
        
        low = 1
        high = n-2

        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid] > nums[mid-1]:
                # increasing order
                low = mid + 1
            elif nums[mid] > nums[mid+1]:
                # decreasing order
                high = mid - 1
            else:
                # edge case ---> [4, 5, 1, 6, 2]
                #                    ^     ^
                high = mid - 1
        