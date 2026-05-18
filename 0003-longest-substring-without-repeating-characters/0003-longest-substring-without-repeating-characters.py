class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        maxLen = 0
        hashMap = {}
        while( r < n):
            if( s[r] in hashMap ):
                l = max(l, hashMap[s[r]] + 1)
            hashMap[s[r]] = r
            maxLen = max( maxLen, r - l + 1)
            r += 1
        return maxLen