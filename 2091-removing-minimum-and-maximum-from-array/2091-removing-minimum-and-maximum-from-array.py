class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        # from front side
        front = max(minIndex, maxIndex) + 1

        # form back side
        back = n - min(minIndex, maxIndex)

        # from both side
        both = min(
            (minIndex + 1) + (n - maxIndex),
            (maxIndex + 1) + (n - minIndex)
        )

        return min(front, back, both)