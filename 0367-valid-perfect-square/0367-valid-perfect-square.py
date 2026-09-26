class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search

        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            val = mid * mid
            if val == num:
                return True
            elif val < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
