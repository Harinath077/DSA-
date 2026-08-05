class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {0:1}
        prefixSum = 0
        count = 0
        for num in nums:

            # prefix count

            prefixSum += num

            rem = prefixSum % k
            # rem = ( rem + k ) % k
            if rem in freq:
                count += freq.get(rem, 0)

            freq[rem] = freq.get(rem, 0) + 1
        
        return count