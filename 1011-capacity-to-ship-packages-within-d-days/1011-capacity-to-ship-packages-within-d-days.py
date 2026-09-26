class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def noOfDays(capacity):

            days = 1
            load = 0

            for weight in weights:
                if load + weight > capacity:
                    load = weight
                    days += 1
                else:
                    load += weight
            return days
                    

        low = max(weights)
        high = sum(weights)
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2

            dayRequired = noOfDays(mid)
            if dayRequired <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans