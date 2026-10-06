# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        def dfs(node, row, col):
            if not node:
                return
            
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        nodes = []
        mapp = {}

        # collect node with priority
        dfs(root, 0, 0)

        # sort
        nodes.sort()

        # Group by col
        for col, row, val in nodes:
            if col not in mapp:
                mapp[col] = []
            mapp[col].append(val)
        
        # bulid answer
        res = []
        for col in mapp.keys():
            res.append( mapp[col] )
        return res