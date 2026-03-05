class Solution {
    private int zero(String s, int n){
        int cnt = 0;
        if( s.charAt(0) == '1') cnt++;
        // if index is even ==> 0
        // if index is odd ==> 1
        int index = 0;
        while( index < n - 1){
            if( index % 2 == 0){
                if( '0' == s.charAt( index + 1)){
                    cnt++;
                }
            }else{
                if( '1' == s.charAt(index + 1)){
                    cnt++;
                }
            }
            index++;
        }
        return cnt;

    }

    private int one(String s, int n){
        int cnt = 0;
        if( s.charAt(0) == '0') cnt++;
        // if index is even ==> 1
        // if index is odd ==> 0
        int index = 0;
        while( index < n - 1){
            if( index % 2 == 0){
                if( '1' == s.charAt( index + 1)){
                    cnt++;
                }
            }else{
                if( '0' == s.charAt(index + 1)){
                    cnt++;
                }
            }
            index++;
        }
        return cnt;
    }
    public int minOperations(String s) {
        // base case 
        if( s.length() <= 1){
            return 0;
        }
        int n = s.length();
        int startWithZero = zero( s, n);
        int startWithOne = one( s, n);
        return Math.min( startWithZero, startWithOne);
    }
}