class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints[:k])
        maxSum = total_sum
        for i in range(1,k+1):
            total_sum = total_sum - cardPoints[k - i] + cardPoints[n - i]
            maxSum = max(maxSum,total_sum)
        return maxSum
        