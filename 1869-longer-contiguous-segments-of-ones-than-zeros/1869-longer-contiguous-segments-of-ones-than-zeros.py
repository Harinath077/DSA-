class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        def contiguous(s, target):
            count = 0
            longest = 0
            for char in s:
                if char == target:
                    count += 1
                    longest = max( longest, count)
                else:
                    count = 0
            return longest
        
        ones = contiguous(s, '1')
        zeros = contiguous(s, '0')

        return ones > zeros