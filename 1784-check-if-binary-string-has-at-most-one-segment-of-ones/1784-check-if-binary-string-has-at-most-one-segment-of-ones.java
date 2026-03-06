class Solution {
    public boolean checkOnesSegment(String s) {
        int n = s.length();
        boolean oneFound = false;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1' && !oneFound) {
                oneFound = true;
            }
            if (oneFound && s.charAt(i) == '1') {
                if (i >= 1 && s.charAt(i - 1) == '0') {
                    return false;
                }
            }
        }
        return true;
    }
}