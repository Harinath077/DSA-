class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # find the longest sequential nums
        n = len(nums)
        sum_ = nums[0]
        set_ = set(nums)
        for i in range(1, n):
            if nums[i]-1 == nums[i-1]:
                sum_ += nums[i]
            else:
                break
    
        ans = sum_

        while ans in set_:
            ans += 1
        return ans
        