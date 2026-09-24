class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        right = bisect.bisect_right(arr, x)
        left = right - 1
        res = []

        while k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= n:
                res.append(arr[left])
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            k -= 1

        return sorted(res)