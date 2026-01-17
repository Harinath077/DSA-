class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        HashMap<Integer, Integer> mapp = new HashMap<>();
        // initialization
        mapp.put(0, 1);
        int prefixSum = 0;
        int count = 0;
        for( int num : nums){
            prefixSum += num & 1;
            if( mapp.containsKey( prefixSum - k)){
                count += mapp.get( prefixSum - k);
            }

            // add in mapp
            mapp.put( prefixSum, mapp.getOrDefault( prefixSum ,0) + 1);
        }
        return count;
    }
}