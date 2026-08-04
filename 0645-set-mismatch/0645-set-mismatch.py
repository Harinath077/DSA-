class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # cyclic sort
        n = len(nums)
        i = 0
        while i < n:

            correctIndex = nums[i]-1

            if nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1
        print(nums)
        # scan to find the missing value
        res = []
        for i in range(n):
            if nums[i]-1 != i:
                res.append( nums[i])
                res.append(i+1)
        
        return res