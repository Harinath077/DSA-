class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        
        setNum = set(arr)
        number = 1
        while True:
            
            if number not in setNum and k > 0:
                k -= 1
            if k == 0:
                return number
            number += 1
            
