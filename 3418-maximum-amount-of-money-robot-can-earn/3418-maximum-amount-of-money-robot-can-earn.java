class Solution {
    int n, m;
    int[][] coins;
    int[][][] memo;

    public int maximumAmount(int[][] coins) {
        this.coins = coins;
        n = coins.length;
        m = coins[0].length;

        // 3D memo: n x m x 3
        memo = new int[n][m][3];

        // initialize with a sentinel (not visited)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 3; k++) {
                    memo[i][j][k] = Integer.MIN_VALUE;
                }
            }
        }

        return helper(0, 0, 2);
    }

    private int helper(int r, int c, int k) {
        // out of bounds
        if (r >= n || c >= m) {
            return Integer.MIN_VALUE / 2; // avoid overflow
        }

        // memo check
        if (memo[r][c][k] != Integer.MIN_VALUE) {
            return memo[r][c][k];
        }

        int value = coins[r][c];

        // destination
        if (r == n - 1 && c == m - 1) {
            if (value < 0 && k > 0) {
                return memo[r][c][k] = 0;
            }
            return memo[r][c][k] = value;
        }

        // option 1: take value
        int take = value + Math.max(
            helper(r, c + 1, k),
            helper(r + 1, c, k)
        );

        // option 2: neutralize robber
        int skip = Integer.MIN_VALUE;
        if (value < 0 && k > 0) {
            skip = Math.max(
                helper(r, c + 1, k - 1),
                helper(r + 1, c, k - 1)
            );
        }

        memo[r][c][k] = Math.max(take, skip);
        return memo[r][c][k];
    }
}