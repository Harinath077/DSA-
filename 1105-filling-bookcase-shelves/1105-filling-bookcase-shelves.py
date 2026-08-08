
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        # recursion definition
      
        def helper(i): # ---> return the minimum height need for the books to add in shelf form 0 -> i books

            # base case
            if i == n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            minHeight = float('inf')
            maxHeight = 0
            currWidth = 0
            # decision spliter
            for j in range(i, n):

                thickness, height = books[j]
                currWidth += thickness

                # edge case
                if currWidth > shelfWidth:
                    break
                
                # tracking height for this shelf
                maxHeight = max( height, maxHeight )
                
                # tracking for this decision tree / branch
                totalHeight = maxHeight + helper( j + 1 )
                minHeight = min( totalHeight , minHeight)

            memo[i] = minHeight
            return memo[i]

        n = len(books)
        memo = [-1] * n
        return helper(0)

                

        