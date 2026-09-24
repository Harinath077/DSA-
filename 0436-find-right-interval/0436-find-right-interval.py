class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        def lowerBound(arr, target):
            n = len(arr)
            low = 0
            high = n-1
            ans = -1
            while low <= high:
                mid = low + (high - low)//2
                if arr[mid][0] >= target:
                    ans = arr[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
                

        n = len(intervals)
        starts = []
        res = []
        for i in range(n):
            starts.append(( intervals[i][0], i))
        
        # sort respect to values
        starts.sort()
        
        for i in range(n):
            end = intervals[i][1]
            index = lowerBound(starts, end)
            res.append(index)
        return res
