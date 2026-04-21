
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = {}
        def helper(ind, curSum):
            if ind < 0:
                if curSum == target:
                    return 1
                else:
                    return 0
            if( ind, curSum ) in memo:
                return memo[(ind,curSum)]

            pluse = helper(ind - 1, curSum + nums[ind])
            minus = helper(ind - 1, curSum - nums[ind])
            memo[(ind,curSum)] =  pluse + minus
            return memo[(ind,curSum)]
        return helper(n-1,0)