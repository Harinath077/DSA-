class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        prev = [0] * m
        
        # Initialize first row
        prev[0] = grid[0][0]
        for j in range(1, m):
            prev[j] = prev[j-1] + grid[0][j]
        
        for i in range(1, n):
            curr = [0] * m
            
            # First column
            curr[0] = grid[i][0] + prev[0]
            
            for j in range(1, m):
                up = grid[i][j] + prev[j]
                left = grid[i][j] + curr[j-1]
                curr[j] = min(up, left)
            
            prev = curr
        
        return prev[m-1]