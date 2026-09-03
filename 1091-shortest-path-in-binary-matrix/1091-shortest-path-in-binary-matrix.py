class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        # edge case: blocked start or end
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
            
        # intialization 
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (-1, 1), (1, -1), (1, 1), (-1, -1)
        ]
        queue = deque([(0, 0, 1)]) # (row, col, length)

        while queue:
            row, col , length = queue.popleft()

            if row == n-1 and col == n-1:
                return length

            for dr, dc in directions:

                nr = dr + row
                nc = dc + col

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append( (nr, nc, length + 1) )

        return -1
