# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        maxWidth = -1
        
        while queue:
            first = 0
            last = 0
            size = len(queue)
            minIdx = queue[0][1]

            for i in range(size):
                node, index = queue.popleft()
                index -= minIdx
                
                if i == 0:
                    first = index
                elif i == size - 1:
                    last = index
                # enqueue
                if node.left:
                    queue.append( (node.left, index * 2 + 1))
                if node.right:
                    queue.append( (node.right, index * 2 + 2))

            maxWidth = max(maxWidth, last - first + 1)
        return maxWidth