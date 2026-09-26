class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans