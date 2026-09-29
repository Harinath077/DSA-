from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        if (n + m - 1) % 2 != 0 or grid[0][0] == ')' or grid[n-1][m-1] == '(':
            return False

        @cache
        def dfs(row, col, count):
            if row >= n or col >= m:
                return False
            
            if grid[row][col] == '(':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False
            
            if row == n - 1 and col == m - 1:
                return count == 0
            
            return dfs(row + 1, col, count) or dfs(row, col + 1, count)
        
        return dfs(0, 0, 0)