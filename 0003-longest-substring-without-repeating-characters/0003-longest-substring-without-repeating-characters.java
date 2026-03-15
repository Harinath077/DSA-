class Solution {
    public int lengthOfLongestSubstring(String s) {
        StringBuilder str = new StringBuilder(s);
        int left = 0;
        int right = 0;
        int maxLen = 0;
        HashMap<Character, Integer> charMap = new HashMap<>();

        while( right < str.length()){
            if( charMap.containsKey(str.charAt(right))){
                left = Math.max(left, charMap.get(str.charAt(right)) + 1);
            }
            charMap.put( str.charAt(right), right);
            maxLen = Math.max(maxLen, right - left + 1);
            right++;
        }
        return maxLen;
    }
}