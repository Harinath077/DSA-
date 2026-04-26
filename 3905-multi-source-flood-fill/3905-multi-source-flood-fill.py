class Solution:
    # my key instight is this graph question and multisoure BFS
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for _ in range(n)]
        queue = deque()

        for r, c, color in sources:
            grid[r][c] = color
            queue.append( (r, c) )

        dir = [(-1,0),(0,1),(1,0),(0,-1)]
        while( queue ):

            nextCell = {}

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc

                    if( 0 <= nr < n and 0 <= nc < m):
                        if( grid[nr][nc] == 0):
                            color = grid[r][c]

                            if(nr, nc) not in nextCell:
                                nextCell[(nr,nc)] = color
                            else:
                                nextCell[(nr,nc)] = max( color, nextCell[(nr,nc)])

            for (r, c), color in nextCell.items():
                grid[r][c] = color
                queue.append((r,c))

        return grid

            