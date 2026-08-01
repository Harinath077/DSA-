from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(arr):
            @cache
            def dfs(i):
                if i < 0:
                    return 0
                if i == 0:
                    return arr[0]

                return max(
                    dfs(i - 1),
                    arr[i] + dfs(i - 2)
                )

            return dfs(len(arr) - 1)

        if len(nums) == 1:
            return nums[0]

        return max(
            solve(nums[:-1]),
            solve(nums[1:])
        )