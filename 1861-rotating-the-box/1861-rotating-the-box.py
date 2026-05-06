class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)  # after roatiting it will be the no of cols
        n = len(boxGrid[0]) # after roatiting it will be the no of rows
        result = [["" for _ in range(m)] for _ in range(n)]

        # 1 roatate matrix

        for i in range(n):
            for j in range(m):
                result[i][j] = boxGrid[j][i]
        
        for i in range(n):
            result[i].reverse()
        
        # 2 apply gravity law on GRID BOX

        for j in range(m):

            for i in range(n-1, -1,-1):
                if( result[i][j] == "."):
                    nextRowWithStone = -1

                    for k in range(i-1, -1, -1):
                        if( result[k][j] == "*"):
                            break
                        if( result[k][j] == "#"):
                            nextRowWithStone  = k
                            break
                    
                    # if a stone was found above , let it fall in the pos of "i"
                    if( nextRowWithStone != -1):
                        result[nextRowWithStone][j] = "."
                        result[i][j] = "#"
        
        return result