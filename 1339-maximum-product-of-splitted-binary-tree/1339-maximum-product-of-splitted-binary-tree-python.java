/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private static final int MOD = 1_000_000_007;
    private long totalSum = 0;
    private long maxProduct = 0;

    private long dfsSum(TreeNode node){
        if( node == null ){
            return 0;
        }
        return node.val + dfsSum(node.left) + dfsSum(node.right);
    }

    private long dfs(TreeNode node){
        if(node == null){
            return 0;
        }

        long left = dfs(node.left);
        long right = dfs(node.right);

        long subTreeSum = node.val + left + right;

        maxProduct = Math.max(
            maxProduct,
            subTreeSum * ( totalSum - subTreeSum)
        );

        return subTreeSum;
    }
    public int maxProduct(TreeNode root) {
        
        totalSum = dfsSum(root);

        dfs(root);

        return (int) (maxProduct % MOD);
    }
}