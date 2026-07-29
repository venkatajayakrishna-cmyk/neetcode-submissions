# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfsInvert(self, root):
        if not root:
            return root
        
        root.right, root.left = root.left, root.right

        if root.left:
            self.dfsInvert(root.left)
        
        if root.right:
            self.dfsInvert(root.right)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.dfsInvert(root)
        return root