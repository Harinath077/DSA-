class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            # Choice 1: Include nums[index]
            include = dfs(index + 1, current_xor ^ nums[index])
            # Choice 2: Exclude nums[index]
            exclude = dfs(index + 1, current_xor)
            return include + exclude
        
        return dfs(0, 0)
