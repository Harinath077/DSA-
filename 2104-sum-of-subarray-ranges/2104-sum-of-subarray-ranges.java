class Solution {
    public long subArrayRanges(int[] nums) {
        int n = nums.length;
        long total = 0; // Using long to prevent integer overflow

        for (int i = 0; i < n; i++) {
            int min_ = nums[i];
            int max_ = nums[i];

            for (int j = i; j < n; j++) {
                min_ = Math.min(min_, nums[j]);
                max_ = Math.max(max_, nums[j]);
                total += (max_ - min_);
            }
        }
        return (long) total; // Casting back to int as per the problem constraints
    
    }
}