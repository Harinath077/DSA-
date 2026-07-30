class Solution:
    def minimumPushes(self, word: str) -> int:
        def helper(n, level):
            # base case
            if n == 0:
                return n
            if n <= 8:
                return n * level
            return 8 * level + helper(n -8, level+1)
        n = len(word)
        return helper(n, 1)