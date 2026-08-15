class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        longest = -1
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                if freq[s[j]] > 2:
                    break
                longest = max( longest, j - i + 1)
        
        return longest