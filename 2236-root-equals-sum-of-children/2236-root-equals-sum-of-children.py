# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        
        if not root or not root.left or not root.right:
            return True
        
        sum_ = 0
        if root.left:
            sum_ += root.left.val
        if root.right:
            sum_ += root.right.val       
        # main check
        if root.val == sum_:
            return self.checkTree(root.left) and self.checkTree(root.right)
        else:
            return False