class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)

        prefix_max = [0] * n
        prefix_gcd = [0] * n

        prefix_max[0] = nums[0]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        for i in range(n):
            prefix_gcd[i] = gcd(prefix_max[i], nums[i])

        prefix_gcd.sort()

        res = 0

        for i in range(n // 2):
            res += gcd(prefix_gcd[i], prefix_gcd[n - i - 1])

        return res