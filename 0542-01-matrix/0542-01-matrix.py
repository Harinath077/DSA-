from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])

        visited = [[False] * m for _ in range(n)]
        distance = [[-1] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()

        # enqueue the element who's value is 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append( (i, j) )
                    visited[i][j] = True
                    distance[i][j] = 0
        
        # bfs -- level by level with multi source 
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                        visited[nr][nc] = True
                        distance[nr][nc] = distance[r][c] + 1
                        queue.append( (nr, nc) )
        
        return distance