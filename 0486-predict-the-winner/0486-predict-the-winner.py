from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def dfs(left, right):

            # base case
            if left == right:
                return nums[left]
            
            pickLeft = nums[left] - dfs(left + 1, right)
            pickRight = nums[right] - dfs(left, right -1)

            return max(pickLeft, pickRight)

         # If Player 1's advantage is non-negative, he wins (or ties)
        return dfs(0, len(nums) - 1) >= 0