
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        # dp[i]  ---> return the minimum height need for the books to add in shelf form 0 -> i books

        n = len(books)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
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
                totalHeight = maxHeight + dp[j + 1]
                minHeight = min( totalHeight , minHeight)

            dp[i] = minHeight
            
        return dp[0]

                

        