class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapp = {}
        for i in range(n):
            need = target - nums[i]

            if( need in mapp ):
                return [mapp[need],i]
            mapp[nums[i]] = i
        