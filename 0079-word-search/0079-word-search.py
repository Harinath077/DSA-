class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, index, visited):
            # base case
            if index == len(word):
                return True
            # False case
            if ( r < 0 or r >= row or 
                 c < 0 or c >= col or
                 (r,c) in visited or
                 board[r][c] != word[index]):
                  return False
            visited.add((r,c))
            found = ( dfs(r+1, c, index+1, visited) or
                      dfs(r-1, c, index+1, visited) or 
                      dfs(r, c+1, index+1, visited) or
                      dfs(r, c-1, index+1, visited) )
            visited.remove((r,c))
            return found
    
        row, col = len(board), len(board[0])
        visited = set()
        index = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, index, visited):
                        return True
        return False
