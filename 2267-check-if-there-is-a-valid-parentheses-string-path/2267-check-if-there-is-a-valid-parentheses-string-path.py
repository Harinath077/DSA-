class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        @cache
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

            down = dfs(row, col + 1, count)
            right = dfs(row + 1, col, count)

            return down or right
        
        n = len(grid)
        m = len(grid[0])
        return dfs(0, 0, 0)