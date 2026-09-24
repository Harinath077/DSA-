class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []

        for num in arr:
            temp.append((abs(num - x), num))

        # Sort by distance first, then by value
        temp.sort()

        res = []

        for i in range(k):
            res.append(temp[i][1])

        res.sort()

        return res