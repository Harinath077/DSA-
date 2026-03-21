class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        def helper(index, ds):
            if( index == len(nums)):
                if sum(ds) == target:
                    result.add(tuple(ds.copy()))
                return
            ds.append(nums[index])
            helper(index + 1, ds)
            ds.pop()
            helper(index + 1, ds)
        helper(0, [])
        return list(result)
