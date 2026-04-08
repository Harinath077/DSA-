class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return False

        @lru_cache(None)
        def dfs(index, count):
            if(count < 0):
                return False
            if(index == len(s)):
                return count == 0
            
            # ch = '('
            if s[index] == '(':
                return dfs(index + 1, count + 1)
            # ch == ')
            elif s[index] == ')':
                return dfs(index + 1, count - 1)
            else:
                # try three possible ways
                return (
                    dfs(index + 1, count + 1) or
                    dfs(index + 1, count ) or
                    dfs(index + 1,count - 1)
                )
            return False
        return dfs(0, 0)
    