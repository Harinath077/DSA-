# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # base case
        if not root or root == p or root == q:
            return root
            
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        # if both exisit found LCA 
        if leftLCA and rightLCA:
            return root
        else: # if only node exisits --> means simply pass upwards
            if not leftLCA:
                return rightLCA
            else:
                return leftLCA
        