import java.util.*;
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Set<List<Integer>> result = new HashSet<>();
        int n = nums.length;
        for(int i = 0; i < n ; i++){
            for(int j = i+1; j < n; j++){
                Set<Integer> seen = new HashSet<>();
                for(int k = j + 1; k < n; k++){
                    long sum = (long)nums[i] + nums[j] + nums[k];
                    long fourth = target - sum;

                    if( fourth >= Integer.MIN_VALUE && fourth <= Integer.MAX_VALUE 
                        && seen.contains((int)fourth) ){
                        List<Integer> pair = Arrays.asList( nums[i], nums[j], nums[k], (int)fourth);
                        Collections.sort(pair);
                        result.add( pair );
                    }
                    seen.add( nums[k]);
                }
            }
        }
        return new ArrayList<>(result);
    }
}