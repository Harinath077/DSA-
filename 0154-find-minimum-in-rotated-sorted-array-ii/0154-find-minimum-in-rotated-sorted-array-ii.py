class Solution:
    def findMin(self, arr: List[int]) -> int:
        
        n = len(arr)
        low, high = 0, n - 1
        min_ = float("inf")

        while low <= high:
            mid = (low + high) // 2

            # edage case[duplicate]
            if arr[low] == arr[high] and low < high:
                low += 1
                continue            
            # If the subarray is sorted, update min_ and exit
            if arr[low] <= arr[high]:
                min_ = min(min_, arr[low])
                break

            # Left part is sorted
            if arr[low] <= arr[mid]:
                min_ = min(min_, arr[low])
                low = mid + 1
            # Right part is sorted
            else:
                min_ = min(min_, arr[mid])
                high = mid - 1

        return min_
