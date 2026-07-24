class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        pairs_ij = set()

        for i in range(n):
            for j in range(n):
                pairs_ij.add( nums[i] ^ nums[j] )

        res = set()
        for p in pairs_ij:
            for num in nums:
                res.add( p ^ num )
        
        return len(res)