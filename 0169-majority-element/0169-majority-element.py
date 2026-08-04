class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        me = nums[0]
        count = 1

        for i in range(1, n):
            if me == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                me = nums[i]
                count = 1
        
        return me
        