class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        temp = nums[:]

        for i in range(n):
            if temp[i] == 0:
                temp[i] = -1
        
        prefixSum = 0
        maxLen = 0
        mapp = {0:-1} # {prefixSum, firstIndex}

        for i in range(n):
            prefixSum += temp[i]

            if prefixSum in mapp:
                first = mapp[prefixSum]
                maxLen = max( i - first, maxLen)
            else:
                mapp[prefixSum] = i
        return maxLen
            

