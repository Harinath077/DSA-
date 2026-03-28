class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative numbers
        pos = []
        neg = []
        
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        # Create result array
        res = [0] * len(nums)

        # Rearranging elements: positives at even indices, negatives at odd indices
        i = 0
        while i < len(pos) and i < len(neg):
            res[2 * i] = pos[i]
            res[2 * i + 1] = neg[i]
            i += 1

        # If there are remaining elements
        if i < len(pos):
            res[2 * i:] = pos[i:]
        elif i < len(neg):
            res[2 * i:] = neg[i:]

        return res