class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        low = 0
        high = x 
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            val = mid * mid
            if val > x:
                high = mid - 1
            else:
                ans = mid 
                low = mid + 1
        return ans