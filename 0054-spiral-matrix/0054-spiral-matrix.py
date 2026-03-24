class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        result = []
        top , left = 0, 0
        right , bottom = m -1, n-1

        while left <= right and top <= bottom:
            #left --> rigth
            for i in range(left,right + 1):
                result.append(matrix[top][i])
            top += 1

            #top --> bottom
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -=  1

            #rigth --> left
            if top <= bottom:
                for i in range(right , left -1 ,-1 ):
                    result.append(matrix[bottom][i])
                bottom -= 1
            #bottom --> top
            if left <= right:
                for i in range(bottom , top - 1,-1 ):
                    result.append(matrix[i][left])
                left += 1
        return result
        