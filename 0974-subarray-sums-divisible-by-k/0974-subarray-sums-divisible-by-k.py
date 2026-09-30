class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        count = 0
        freq = {0:1}
        prefixSum = 0

        for num in nums:

            prefixSum += num

            rem = prefixSum % k

            if rem in freq:
                count += freq[rem]
            
            # count Frequency 
            freq[rem] = freq.get(rem, 0) + 1
        
        return count