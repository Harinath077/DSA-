class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        
        count = 0
        
        for r2 in range(n):
            for c2 in range(m):
                
                # compute sum of submatrix (0,0) → (r2,c2)
                total = 0
                for i in range(r2 + 1):
                    for j in range(c2 + 1):
                        total += grid[i][j]
                
                if total <= k:
                    count += 1
                    
        return count