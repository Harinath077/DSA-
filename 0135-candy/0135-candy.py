class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [0] * n
        right = [0] * n

        # default value intialization
        left[0] = 1
        right[n-1] = 1

        # hadling left increasing slop
        for i in range(1, n):
            if( ratings[i] > ratings[i-1] ):
                left[i] += left[i-1] + 1
            else:
                left[i] = 1
        
        # handling for right increasing slop
        for i in range(n-2, -1, -1):
            if( ratings[i] > ratings[i+1] ):
                right[i] += right[i+1] + 1
            else:
                right[i] = 1
        
        # find the answering by combaining
        noOfCandies = 0
        for i in range(n):
            noOfCandies += max(left[i], right[i])
        
        return noOfCandies
            