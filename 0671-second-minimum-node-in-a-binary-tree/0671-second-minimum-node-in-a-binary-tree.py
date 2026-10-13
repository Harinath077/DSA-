# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
       
        first = float('inf')
        second = float('inf')
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.val < first:
                    second = first
                    first = node.val
                elif node.val < second and node.val != first:
                    second = node.val
                
                # enqueue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return second if second != float('inf') else -1