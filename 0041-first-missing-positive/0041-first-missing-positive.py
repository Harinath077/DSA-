class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # edge case : 1 itself missing
        if n == 1 and (nums[0] > 1 or nums[0] < 1):
            return 1
        
        set_ = set(nums)
     

        for num in range(1,n+1):
            if num not in set_:
                return num
        return n+1
        


        
