from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        @lru_cache(None)
        def helper(ind, curSum):
            if ind < 0:
                if curSum == target:
                    return 1
                else:
                    return 0
            
            pluse = helper(ind - 1, curSum + nums[ind])
            minus = helper(ind - 1, curSum - nums[ind])
            return pluse + minus
        return helper(n-1,0)