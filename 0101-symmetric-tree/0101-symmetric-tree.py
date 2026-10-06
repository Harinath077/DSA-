# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        # same as DFS in BFS

        if not root:
            return False
        
        queue = deque([(root.left, root.right)])

        while queue:
            r1, r2 = queue.popleft()

            # if both are empty ---> continue
            if not r1 and not r2:
                continue
            
            # if any one empty (or) value NOT EQUAL
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            
            # Enqueue
            queue.append((r1.left, r2.right))
            queue.append((r1.right, r2.left))
        return True
