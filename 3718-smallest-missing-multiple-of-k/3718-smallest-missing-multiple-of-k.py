class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        multiple = k

        while True:
            if multiple not in seen:
                return multiple
            multiple += k
        