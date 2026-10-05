# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # edge case
        if not root:
            return []
        queue = deque([root])
        res = []
        leftToRight = True

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append( node.val )
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not leftToRight:
                level.reverse()
                
            res.append( level )
            leftToRight = not leftToRight
        return res