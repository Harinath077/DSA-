class Solution:
    def isBalanced(self, mapp):
        return len(set(mapp.values())) == 1      
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return n
        
        
        longLen = float('-inf')
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get( s[j], 0) + 1
                if self.isBalanced(freq):
                    longLen = max(longLen, j - i + 1)
                
        return longLen