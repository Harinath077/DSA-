# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node):
        if node is None:
            return 0
        
        leftH = self.getHeight(node.left)
        rightH = self.getHeight(node.right)
        return 1 + max(leftH, rightH)

    def isBalanced(self, root: TreeNode | None) -> bool:
        
        if not root:
            return True
        
        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)

        if abs( leftH - rightH) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False