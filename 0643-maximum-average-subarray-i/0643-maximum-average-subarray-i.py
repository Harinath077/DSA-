class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        l = 0
        r = 0
        n = len(nums)
        currSum = 0
        maxAvg = float('-inf')

        while r < n:
            currSum += nums[r]

            if r-l+1 > k:
                currSum -= nums[l]
                l += 1
            if r-l+1 == k:
                maxAvg = max( maxAvg, currSum / k)
            r += 1
        return maxAvg
