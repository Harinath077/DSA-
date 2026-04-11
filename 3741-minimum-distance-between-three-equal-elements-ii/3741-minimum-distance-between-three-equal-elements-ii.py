class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        next_ = [-1] * n
        occurs = {}

        # building the next_[]
        for i in range(n - 1, -1, -1):
            if( nums[i] in occurs):
                next_[i] = occurs[nums[i]]
            occurs[nums[i]] = i
        
        # find the minDist
        minDist = float('inf')

        for i in range(n):
            second = next_[i]
            if( second != -1):
                third = next_[second]
                if( third != -1):
                    minDist = min( minDist, (third - i))
        return minDist * 2 if( minDist != float('inf')) else -1