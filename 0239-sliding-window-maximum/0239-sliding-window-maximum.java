class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;  // Changed from arr to nums
        Deque<Integer> dq = new ArrayDeque<>();
        ArrayList<Integer> res = new ArrayList<>();

        for(int i = 0; i < n; i++){
            // remove element out of window
            if(!dq.isEmpty() && dq.getFirst() < i - k + 1){
                dq.pollFirst();
            }
            // decreasing monotonic deque
            while(!dq.isEmpty() && nums[dq.getLast()] < nums[i]){  // Changed arr to nums
                dq.pollLast();
            }
            dq.offerLast(i);

            // for res
            if(i >= k - 1){
                res.add(nums[dq.getFirst()]);  // Changed arr to nums
            }
        }
        
        // Convert ArrayList to int[]
        int[] result = new int[res.size()];
        for(int i = 0; i < res.size(); i++){
            result[i] = res.get(i);
        }
        return result;
    }
}