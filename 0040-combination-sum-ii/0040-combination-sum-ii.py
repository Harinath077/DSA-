class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def helper(index, target, ds):
            if target == 0:
                result.append(ds.copy())
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    break
                ds.append(nums[i])
                helper(i+1, target-nums[i], ds)
                ds.pop()
            
        helper(0, target, [])
        return result