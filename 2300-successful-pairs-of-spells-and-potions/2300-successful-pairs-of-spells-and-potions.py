class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        def search(arr, target):
            low = 0
            high = m-1
            ans = -1
            while low <= high:
                mid = low + ( high - low ) // 2
                if arr[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans 

        n = len(spells)
        m = len(potions)
        res = []
        # sort potions
        potions.sort()
        for spell in spells:
            requiredPotion = math.ceil(success / spell)
            index = search( potions, requiredPotion )
            if index == -1:
                res.append(0)
                continue
            count = m - index 
            res.append(count)
        return res