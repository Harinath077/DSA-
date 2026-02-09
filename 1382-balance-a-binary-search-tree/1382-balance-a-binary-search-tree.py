# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # s1 : inorder traversal and store in array ( that will be in sorted)
        # s2 : construct the BST

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
            
        
        def buildBST(low, high):
            if( low > high):
                return
            mid = low + (high - low) // 2
            node = TreeNode(values[mid])
            node.left = buildBST(low, mid - 1)
            node.right = buildBST(mid + 1, high)
            return node

        # main execuiton
        values = []
        inorder(root)
        return buildBST(0, len(values) - 1)