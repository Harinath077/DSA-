# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        def dfs(node):
            if node is None:
                return 
            
            dfs(node.left)
            dfs(node.right)
            postorder.append(node.val)
        
        postorder = []
        dfs(root)
        return postorder