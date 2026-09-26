class Solution:
    """  
    piles = [3,6,7,11], h = 8
    k = 2 --> 2 bananas per hour
    [2hr, 3hr, 4hr, 6hs] --> 15 > 8 X

    k = 4 --> 4 bananas per hour
    [1hr, 2hr, 2hr, 3hr] ---> 8hr correct answer

    """
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # range -- > 1 - max(arr) + 1
        ans = -1
        low = 1
        high = max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            totalHour = sum( math.ceil(pile/mid) for pile in piles )
            if totalHour <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
