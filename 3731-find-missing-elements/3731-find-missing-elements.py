class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        ptr = 0
        res = []
        for num in range(nums[0], nums[-1] + 1):
            if num != nums[ptr]:
                res.append(num)
            else:
                ptr += 1
        return res
