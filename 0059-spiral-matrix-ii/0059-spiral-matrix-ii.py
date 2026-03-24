class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        # first column
        left = 0
        # last column
        right = n-1
        # first row
        top = 0
        # last row
        bottom = n-1
        value = 1
        mat = []
        while left <= right and top <= bottom:
            # left to right
            for i in range(left,right+1):
                matrix[top][i] = value
                value += 1
            top += 1
            # top to bottom
            for i in  range(top,bottom+1):
                matrix[i][right] = value
                value += 1
            right -= 1

            #left to right 
            for i in range(right, left-1, -1):
                matrix[bottom][i] = value
                value += 1
            bottom -= 1

            #bottom to top
            for i in range(bottom,top-1,-1):
                matrix[i][left] = value
                value += 1
            left += 1
        return matrix

        