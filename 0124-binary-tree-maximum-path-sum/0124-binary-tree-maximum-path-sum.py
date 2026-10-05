# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def maxPath(node):
            
            if not node:
                return 0
            left = max(0, maxPath(node.left) )
            right = max(0, maxPath(node.right) )
            max_[0] = max( max_[0], node.val + left + right)
            return node.val + max(left , right)

        max_ = [float('-inf')]
        maxPath(root)
        return max_[0]