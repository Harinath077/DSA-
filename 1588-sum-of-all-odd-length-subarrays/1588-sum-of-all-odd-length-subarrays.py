class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        oddSum = 0
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += arr[j]
                
                if (j - i + 1) % 2 == 1:
                    oddSum += sum_
        return oddSum