class Solution:
    def flip(self, dummy, x, k):
        top = x
        bottom = x + k - 1
        while( top < bottom):
            dummy[top], dummy[bottom] = dummy[bottom], dummy[top]
            top += 1
            bottom -= 1

    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        n = len(grid)
        m = len(grid[0])
        dummy = [[None]*m for _ in range(n)]
        for i in range(x, x + k ): # range is (x, x + k - 1)
            for j in range(y, y + k ): # range is ( y, y + k - 1)
                dummy[i][j] = grid[i][j]
        self.flip(dummy, x, k)
        for i in range(n):
            for j in range(m):
                if dummy[i][j] == None:
                    dummy[i][j] = grid[i][j]
        return dummy