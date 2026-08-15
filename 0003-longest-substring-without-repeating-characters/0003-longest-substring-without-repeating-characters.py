class Solution:
    """  
    expand ---> if ferq[substring] <= 1
    shrink ---> if freq[substring] > 1

    """
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        maxLen = 0
        freq = {}

        left = 0

        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            maxLen = max( maxLen, right - left + 1)

        return maxLen