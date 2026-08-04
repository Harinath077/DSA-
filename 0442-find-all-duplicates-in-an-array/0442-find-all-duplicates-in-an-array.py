class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        mapp = {}
        result = []
        for i in range(n):
            mapp[nums[i]] = mapp.get(nums[i], 0) + 1
        
        for i in range(1, n + 1):
            if mapp.get(i, 0) > 1:
                result.append(i)
        return result