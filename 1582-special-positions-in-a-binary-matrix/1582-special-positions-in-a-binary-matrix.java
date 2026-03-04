class Solution {
    private int count(int[][] mat, int posi, int posj, int n, int m){
        // check for row
        for( int k = 0; k < m; k++){
            if( mat[posi][k] == 1 && k != posj){
                return 0;
            }
            else if( mat[posi][k] == 0){
                continue;
            }
        }

        // check for column
        for( int z = 0; z < n; z++){
            if( mat[z][posj] == 1 && z != posi){
                return 0;
            }
            else if( mat[z][posj] == 0 ){
                continue;
            }
        }
        return 1;
    }
    public int numSpecial(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int splPos = 0;
        for( int i = 0; i < n; i++){
            for( int j = 0; j < m; j++){
                if( mat[i][j] == 1){
                    splPos += count( mat, i, j, n, m);
                }
            }
        }
        return splPos;
    }
}