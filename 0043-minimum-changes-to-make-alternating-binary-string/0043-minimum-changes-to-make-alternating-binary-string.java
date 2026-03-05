class Solution {
    public int minOperations(String s) {
        int startWithZero = 0;
        int startWithOne = 0;
        int n = s.length();
        for( int i = 0; i < n; i++){
            if( s.charAt(i) != (( i % 2 == 0) ? '0' : '1')){
                startWithZero++;
            }
            if( s.charAt(i) != ((i % 2 == 0) ? '1' : '0')){
                startWithOne++;
            }

        }
        return Math.min( startWithOne, startWithZero);
    }
}