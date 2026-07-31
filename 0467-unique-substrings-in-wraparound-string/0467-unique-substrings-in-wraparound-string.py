class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:

        dp = [0] * 26
        current = 0

        for i in range(len(s)):

            if i > 0 and (
                ord(s[i]) - ord(s[i - 1]) == 1 or
                (s[i - 1] == 'z' and s[i] == 'a')
            ):
                current += 1
            else:
                current = 1

            idx = ord(s[i]) - ord('a')
            dp[idx] = max(dp[idx], current)

        return sum(dp)