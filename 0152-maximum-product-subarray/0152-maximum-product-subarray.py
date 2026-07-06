class Solution:
    def maxProduct(self, nums):

        memo = {}

        def solve(i):
            if i == 0:
                return nums[0], nums[0]
            if i in memo:
                return memo[i]
            prev_max, prev_min = solve(i - 1)

            curr_max = max(
                nums[i],
                prev_max * nums[i],
                prev_min * nums[i]
            )

            curr_min = min(
                nums[i],
                prev_max * nums[i],
                prev_min * nums[i]
            )

            memo[i] = (curr_max, curr_min)
            return memo[i]

        ans = float("-inf")

        for i in range(len(nums)):
            curr_max, _ = solve(i)
            ans = max(ans, curr_max)

        return ans