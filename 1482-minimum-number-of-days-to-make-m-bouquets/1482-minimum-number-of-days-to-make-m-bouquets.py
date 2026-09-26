class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def possibleDay(day):

            count = 0
            noOfBouqet = 0

            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                    if count == k:
                        noOfBouqet += 1
                        count = 0
                else:
                    count = 0
                if noOfBouqet >= m:
                    return True
            
            return False

        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2

            if possibleDay(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
        
    
