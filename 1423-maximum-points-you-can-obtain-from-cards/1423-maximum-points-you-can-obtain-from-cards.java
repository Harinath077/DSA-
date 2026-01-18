class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int[] prefixSum = new int[k + 1];
        int[] suffixSum = new int[k + 1];
        int maxScore = 0;

        // compute prefixSum
        for(int i = 0; i < k ;i++){
            prefixSum[i + 1] = prefixSum[i] + cardPoints[i];
        }

        // compute suffixSum
        for( int j = 0; j < k;j++){
            suffixSum[j + 1] = suffixSum[j] + cardPoints[n - j - 1];
        }

        // find maxScore
        for(int x = 0; x <= k; x++){
            maxScore = Math.max( prefixSum[x] + suffixSum[k - x], maxScore);
        }
        return maxScore;

    }
}