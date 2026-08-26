class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        n = len(s)

        left = 0
        oneCnt = 0
        ans = ""

        for right in range(n):

            if s[right] == '1':
                oneCnt += 1
            
            # Shrink from the left while maintaining or exceeding k ones
            while oneCnt > k or ( left <= right and s[left] == '0' ):
                if s[left] == '1':
                    oneCnt -= 1
                left += 1
            
            # when ever one'== k , evalutate substing with lexicographicalyy 
            if oneCnt == k:
                temp = s[left : right + 1]
                if ans == "" or len(temp) < len(ans) or ( len(temp) == len(ans) and temp < ans):
                    ans = temp
        
        return ans
