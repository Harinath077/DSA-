class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, board, n):
            # Check upper diagonal
            duprow, dupcol = row, col
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            
            # Check left in the same row
            row, col = duprow, dupcol
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
            
            # Check lower diagonal
            row, col = duprow, dupcol
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            
            return True
        
        def solve(col, board, ans, n):
            if col == n:
                ans.append(["".join(row) for row in board])
                return
            
            for row in range(n):
                if is_safe(row, col, board, n):
                    board[row][col] = 'Q'
                    solve(col + 1, board, ans, n)
                    board[row][col] = '.'  # Backtrack
        
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0, board, ans, n)
        return ans