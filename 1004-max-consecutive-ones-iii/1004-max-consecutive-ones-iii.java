class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int left = 0;
        int right = 0;
        int maxLen = 0;
        int zeroCount = 0;
        while( right < n){
            if( nums[right] == 0){
                zeroCount++;
            }

            if( zeroCount > k){
                if( nums[left] == 0){
                    zeroCount--;
                }
                left++;
            }

            if( zeroCount <= k){
                maxLen = Math.max( maxLen, right - left + 1);
            }
            right++;
        }
        return maxLen;

        
    }
}