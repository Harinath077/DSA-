# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_h = self.getHeight(root.left)
        right_h = self.getHeight(root.right)

        if abs(left_h - right_h) <= 1 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right):
            return True
        return False