class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        oneFound = False

        for i in range(n):
            if(s[i] == '1' and not oneFound):
                oneFound = True
            if(oneFound and s[i] == '1'):
                if( i >= 1 and s[i-1] == '0'): return False
        return True