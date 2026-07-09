class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix_max = [0] * n
        prefix_max[0] = nums[0]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        ans = 0

        # i <= j - k
        for j in range(k, n):
            ans = max( prefix_max[j-k] + nums[j], ans)

        return ans