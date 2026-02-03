from typing import List

class Solution:
    def isStrictlyIncreasing(self, arr: List[int]) -> bool:
        return all(arr[i] < arr[i+1] for i in range(len(arr) - 1))

    def isStrictlyDecreasing(self, arr: List[int]) -> bool:
        return all(arr[i] > arr[i+1] for i in range(len(arr) - 1))

    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 2):  # leave at least 2 for mid and 2 for end
            for q in range(p + 1, n - 1):
                first = nums[:p+1]
                second = nums[p:q+1]
                third = nums[q:]

                if (
                    len(first) >= 2 and self.isStrictlyIncreasing(first) and
                    len(second) >= 2 and self.isStrictlyDecreasing(second) and
                    len(third) >= 2 and self.isStrictlyIncreasing(third)
                ):
                    return True
        return False
