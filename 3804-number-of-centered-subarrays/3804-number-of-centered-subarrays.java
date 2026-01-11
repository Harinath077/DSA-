class Solution {
    public int centeredSubarrays(int[] nums) {
        int n = nums.length;
        int count = 0;

        // build prefix sum: pref[i] = nums[0] + ... + nums[i]
        int[] pref = new int[n];
        pref[0] = nums[0];
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + nums[i];
        }

        // check all subarrays nums[i..j]
        for (int i = 0; i < n; i++) {
            HashSet<Integer> set = new HashSet<>();
            for (int j = i; j < n; j++) {

                // grow set for membership check
                set.add(nums[j]);

                // compute sum(i..j) using your prefix style
                int sum;
                if (i == 0) {
                    sum = pref[j];
                } else {
                    sum = pref[j] - pref[i - 1];
                }

                // check condition
                if (set.contains(sum)) {
                    count++;
                }
            }
        }

        return count;
    }
}
