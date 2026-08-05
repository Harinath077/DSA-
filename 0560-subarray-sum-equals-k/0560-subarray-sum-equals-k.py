class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq = {0:1} # {prefixSum : count}
        prefixSum = 0
        count = 0

        for num in nums:

            prefixSum += num

            if prefixSum - k in freq:
                count += freq[prefixSum - k]
            
            if prefixSum not in freq:
                freq[prefixSum] = 1
            else:
                freq[prefixSum] += 1
        return count