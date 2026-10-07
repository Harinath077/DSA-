# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def pathFinding(node, target):
           
            def dfs(node):
                if not node:
                    return False
                path.append(node)
                if node == target:
                    return True
                if dfs(node.left) or dfs(node.right):
                    return True
                # backtrack
                path.pop()
                return False

            path = []
            dfs(node)
            return path

        pathP = pathFinding(root, p)
        pathQ = pathFinding(root, q)
        
        # debuggin 
        print([node.val for node in pathP])
        print([node.val for node in pathQ])

        # traversal and find the LCA
        i = 0
        while i < len(pathP) and \
            i < len(pathQ) and \
            pathP[i] == pathQ[i]:
            i += 1
        return pathP[i-1]

        