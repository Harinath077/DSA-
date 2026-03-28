class Solution:
    def isPalindrome(self, s):
        low = 0
        high = len(s)-1
        while (low < high):
            if( s[high] != s[low]):
                return False
            high -= 1
            low += 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs( index, ds):
            # base case
            if( index == len(s)):
                result.append( ds.copy())
            
            for i in range(index, len(s)):
                if( self.isPalindrome(s[index : i + 1]) ):
                    ds.append(s[index : i + 1])
                    dfs(i + 1, ds)
                    ds.pop()
        dfs(0,[])
        return result