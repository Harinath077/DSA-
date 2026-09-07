class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # All existing subsequences + this character
            dp[i] = (1 + sum(dp)) % MOD

        return sum(dp) % MOD