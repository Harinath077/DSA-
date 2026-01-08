class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            if( i == n or j == m):
                return float('-inf')
            take = nums1[i] * nums2[j]

            # Option 1: take and continue
            take += max(0, helper(i+1, j+1))

            # Option 2: skip in nums1
            skip1 = helper(i+1, j)

            # Option 3: skip in nums2
            skip2 = helper(i, j+1)

            return max(take, skip1, skip2)
        n = len(nums1)
        m = len(nums2)

        return helper(0,0)