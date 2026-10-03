# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node):

            if node is None:
                return 0
            lh = dfs(node.left)
            if lh == -1:
                return -1
            rh = dfs(node.right)
            if rh == -1:
                return -1
            # balance height check
            if abs(lh - rh) > 1:
                return -1
            
            return 1 + max(lh, rh)
        
        return dfs(root) != -1