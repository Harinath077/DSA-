class Solution:
    def exist(self, board, word):
        row, col = len(board), len(board[0])

        def dfs(r, c, index):
            # ✅ base case
            if index == len(word):
                return True

            # ❌ invalid cases
            if (r < 0 or r >= row or
                c < 0 or c >= col or
                board[r][c] != word[index]):
                return False

            # 🔒 mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # 🔍 explore
            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

            # 🔙 restore (backtrack)
            board[r][c] = temp

            return found

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False