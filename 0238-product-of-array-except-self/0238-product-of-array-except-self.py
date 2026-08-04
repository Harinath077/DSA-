class Solution:
    """ 
    prefix = [1, 2, 6, 24]
    suffic = [24, 24, 12,4]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # prefixProduct
        prefix = [1] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        # suffixProdcut
        suffix = [1] * n
        suffix[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        ans = [1] * n
        for i in range(n):
            a = prefix[i-1] if i > 0 else 1
            b = suffix[i+1] if i < n - 1 else 1
            ans[i] = a * b
        
        return ans
