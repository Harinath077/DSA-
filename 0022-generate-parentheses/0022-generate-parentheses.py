class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def helper(openCnt, closeCnt):

            if openCnt == n and closeCnt == n:
                res.append(''.join(ds))
                return n
            
            if openCnt < n:
                ds.append( '(' )
                helper(openCnt + 1, closeCnt)
                ds.pop()
            if closeCnt < openCnt:
                ds.append( ')' )
                helper(openCnt, closeCnt + 1)
                ds.pop()
        
        ds = []
        res = []
        helper(0, 0)
        return res