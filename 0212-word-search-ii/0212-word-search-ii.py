class Solution:
    def findWords(self, board, words):
        row, col = len(board), len(board[0])
        word_set = set(words)
        prefix = set()
        for word in words:
            for j in range(len(word)):
                prefix.add(word[:j+1])
        result = set()
        
        def dfs(r, c, ds):
            if (r < 0 or r >= row or c < 0 or c >= col or board[r][c] == '#' ):
                return
            ds += board[r][c]
            
            if ds not in prefix:
                return  
            if ds in word_set:
                result.add(ds)
            temp = board[r][c]
            board[r][c] = '#'
            
            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr , c + dc, ds)
            # backtracking
            board[r][c] = temp
        
        for i in range(row):
            for j in range(col):
                dfs(i, j, "")
        return list(result)