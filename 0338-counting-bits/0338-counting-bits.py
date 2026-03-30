class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            ones = bin(i).count('1')
            result.append(ones)
        return result