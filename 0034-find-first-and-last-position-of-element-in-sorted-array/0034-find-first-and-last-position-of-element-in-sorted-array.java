class Solution {

    // ----------- LOWER BOUND (first index >= target) -----------
    private int lowerBound(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        int ans = nums.length;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    // ----------- UPPER BOUND (first index > target) -----------
    private int upperBound(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        int ans = nums.length;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] > target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    // ----------- MAIN FUNCTION -----------
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[]{-1, -1};

        if (nums.length == 0) return res;

        int lb = lowerBound(nums, target);

        // validation: target does not exist
        if (lb == nums.length || nums[lb] != target) {
            return res;
        }

        int ub = upperBound(nums, target);

        res[0] = lb;
        res[1] = ub - 1;
        return res;
    }
}
