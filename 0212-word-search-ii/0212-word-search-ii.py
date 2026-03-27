class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        word_set = set(words)
        prefix_set = set()

        # Build all prefixes
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i+1])

        result = set()

        def dfs(r, c, path):
            if (r < 0 or r >= row or c < 0 or c >= col or board[r][c] == "#"):
                return

            path += board[r][c]

            if path not in prefix_set:
                return

            if path in word_set:
                result.add(path)

            temp = board[r][c]
            board[r][c] = "#"  # Mark visited

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r+dr, c+dc, path)

            board[r][c] = temp  # Unmark visited

        # Start DFS from each cell
        for i in range(row):
            for j in range(col):
                dfs(i, j, "")

        return list(result)
