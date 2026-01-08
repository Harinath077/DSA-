class Solution {
    public int lengthOfLongestSubstring(String s) {
        StringBuilder str = new StringBuilder(s);
        int maxLen = 0;
        HashSet<Character> set = new HashSet<>();
        int left = 0;
        int right = 0;

        while (right < str.length()) {

            while (set.contains(str.charAt(right))) {
                set.remove(str.charAt(left));
                left++;
            }
            set.add(str.charAt(right));
            maxLen = Math.max(maxLen, right - left + 1);
            right++;
        }
        return maxLen;
    }
}