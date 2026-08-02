from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def helper(s, e, turn, p1Score, p2Score ):

            # base case
            if s > e:
                return p1Score >= p2Score

            # player
            if turn == 0:
                left = p1Score + nums[s]
                right = p1Score + nums[e]
                
                return helper(s+1, e, 1, left, p2Score) or helper(s, e-1, 1, right, p2Score)
            
            if turn == 1:
                left = p2Score + nums[s]
                right = p2Score + nums[e]
                
                return helper(s+1, e, 0, p1Score, left) and helper(s, e-1, 0, p1Score, right)
            
                            

        
        n = len(nums)

        return helper(0, n-1, 0, 0, 0)