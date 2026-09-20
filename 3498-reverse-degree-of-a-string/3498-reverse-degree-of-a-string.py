class Solution:
    def reverseDegree(self, s: str) -> int:
        
        res = 0
        for index, char in enumerate(s, 1):
            # for reversed flow ( a -> 26, b -> 25 ..... z -> 1 )
            res += ((ord('z') - ord(char)) + 1) * index 
        
        return res
