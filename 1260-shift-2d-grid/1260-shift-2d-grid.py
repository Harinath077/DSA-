class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shifting(i, j, old):
            new = [ row[:] for row in old]
            val1 = []
            for i in range(n):
                val1.append( old[i][m-1] )
            for i in range(n-1):
                for j in range(m-1):
                   new[i][j+1] = old[i][j]
            # last condition
            new[0][0] = val1[n-1]

            for i in range(1,m):
                new[n-1][i] = old[n-1][i-1]
            
            for i in range(1, n):
                new[i][0] = val1[i-1]
            return new

        n = len(grid)
        m = len(grid[0])
        old = grid[:]
        
        for _ in range(k):
            new = shifting(0, 0, old)
            old = new
        return old


        