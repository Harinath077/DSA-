class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        def dfs(row, col, count):

            if row >= n or col >= m:
                return False

            if grid[row][col] == '(':
                    count += 1
            elif grid[row][col] == ')':
                count -= 1

            if count < 0:
                return False

            if row == n-1 and col == m-1:
                if count == 0:
                    return True
                else:
                    return False
            
            if dp[row][col][count] != -1:
                return dp[row][col][count]

            down = dfs(row, col + 1, count)
            right = dfs(row + 1, col, count)

            dp[row][col][count] = down or right
            return dp[row][col][count]
        
        n = len(grid)
        m = len(grid[0])
        countLen = n + m

        dp = [[[-1] * countLen for _ in range(m+1)] for _ in range(n+1)]

        return dfs(0, 0, 0)