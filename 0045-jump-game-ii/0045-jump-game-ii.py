class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l = 0
        r = 0

        while r < n-1:

            farthest = 0

            for index in range(l, r+1):

                farthest = max( farthest, index + nums[index])

            l = r + 1
            r = farthest
            jumps += 1

        return jumps