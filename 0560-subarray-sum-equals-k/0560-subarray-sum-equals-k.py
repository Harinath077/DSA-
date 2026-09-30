class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mapp = {0:1} # { prefixSum, count}

        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            
            if prefixSum - k in mapp:
                count += mapp[prefixSum - k]

            if prefixSum not in mapp:
                mapp[prefixSum] = 1
            else:
                mapp[prefixSum] += 1

        return count