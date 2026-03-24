class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        matCopy = [row[:] for row in matrix]  # safer copy

        maxSize = 0

        for row in range(n):
            for col in range(m):
                if matCopy[row][col] != 0 and row > 0:
                    matCopy[row][col] += matCopy[row - 1][col]

            curRow = matCopy[row][:]
            curRow.sort(reverse=True)

            for i in range(m):  # ✅ fixed
                maxSize = max(maxSize, curRow[i] * (i + 1))

        return maxSize