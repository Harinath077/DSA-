class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                value = board[r][c]

                if (value in rows[r] or
                    value in cols[c] or
                    value in grid[(r//3,c//3)]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                grid[(r//3,c//3)].add(value)
        return True

        