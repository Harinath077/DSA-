class Solution:
    def longestPalindrome(self, s: str) -> int:

        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        n = len(freq)
        evenCnt = 0
        oddCnt = 0
            
        for key, val in freq.items():
            if( val % 2 == 0):
                evenCnt += val
            else:
                evenCnt += val - 1
                oddCnt = 1
        return evenCnt + oddCnt