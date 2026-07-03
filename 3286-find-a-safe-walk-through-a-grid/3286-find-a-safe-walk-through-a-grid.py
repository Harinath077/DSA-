class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])

        best = [[-1] * m for _ in range(n)]

        def dfs(i, j, health):

            # base case 
            if( i < 0 or i >= n or j < 0 or j >= m ):
                return False
            
            health -= grid[i][j]

            if( health <= 0 ):
                return False
            
            if( i == n-1 and j == m-1 ):
                return True
            
            if( best[i][j] >= health ):
                return False
            
            best[i][j] = health

            return ( 
                dfs(i-1, j, health) or
                dfs(i+1, j, health) or
                dfs(i, j-1, health) or
                dfs(i, j+1, health)
            )
        
        return dfs(0, 0, health)

