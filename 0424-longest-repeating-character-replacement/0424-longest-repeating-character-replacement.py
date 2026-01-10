class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        l = 0
        count = [0] * 26
        n = len(s)
        maxLen, maxFreq = 0, 0

        for r in range(n):
            count[ord(s[r]) - ord("A")] += 1
            maxFreq = max(maxFreq, count[ord(s[r]) - ord("A")])
            
            # Adjust the window size when replacements exceed k
            while (r - l + 1) - maxFreq > k:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen


    