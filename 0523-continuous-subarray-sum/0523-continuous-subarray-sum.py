class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefixSum = 0
        first = {0:-1}

        for i, num in enumerate(nums):

            prefixSum += num

            rem = prefixSum % k

            if rem in first:
                if i - first[rem] > 1:
                    return True
            else:
                first[rem] = i
                
        return False
            