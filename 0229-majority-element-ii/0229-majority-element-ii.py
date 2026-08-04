class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        freq = {}
        res = []
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, val in freq.items():
            if val > n // 3:
                res.append(key)
        
        return res