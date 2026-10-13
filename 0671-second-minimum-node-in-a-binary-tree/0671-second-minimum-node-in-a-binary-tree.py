# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        def dfs(node):
            nonlocal first
            nonlocal second
            if not node:
                return 

            if node.val < first:
                second = first
                first = node.val
            elif node.val < second and node.val != first:
                second = node.val
            dfs(node.left)
            dfs(node.right)
        
        first = float('inf')
        second = float('inf')
        dfs(root)
        return second if second != float('inf') else -1