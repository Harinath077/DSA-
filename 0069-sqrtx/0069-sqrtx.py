class Solution:
    def mySqrt(self, x: int) -> int:
        # linear search

        ans = 0
        for num in range(1, x+1):
            val = num * num
            if val <= x:
                ans = num
            else:
                break
        return ans