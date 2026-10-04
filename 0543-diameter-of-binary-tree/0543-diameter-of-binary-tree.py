# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDiameter(node):
            if not node:
                return 0
            
            leftH = getDiameter(node.left)
            rightH = getDiameter(node.right)
            # calculate diameter
            max_[0] = max( max_[0], leftH + rightH)
            return 1 + max( leftH, rightH )

        max_ = [0]
        getDiameter(root)
        return max_[0]