class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # cyclic sort
        n = len(nums)
        i = 0
        while i < n:

            correctIndex = nums[i]

            if nums[i] < n and nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1
        
        # scan to find the missing value

        for i in range(n):
            if nums[i] != i:
                return i
        
        return n