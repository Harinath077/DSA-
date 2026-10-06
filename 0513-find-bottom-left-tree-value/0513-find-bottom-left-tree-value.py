# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        def dfs(node, depth):
            if not node:
                return 
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.ans = node.val
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        self.maxDepth = -1
        self.ans = 0
        dfs(root, 0)
        return self.ans
