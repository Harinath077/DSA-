# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        # optimal BFS approach

        queue = deque([root])
        ans = 0
        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    queue.append( (node.left) )
                if node.right:
                    queue.append( (node.right) )
        return ans
        
        return res[-1][0]
