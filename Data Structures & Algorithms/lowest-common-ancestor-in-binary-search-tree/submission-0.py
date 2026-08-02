# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, a , b):
        if not root:
            return None
        
        if root == a or root == b:
            return root

        left = self.dfs(root.left, a, b)
        right = self.dfs(root.right, a, b)

        if left and right:
            return root
        
        return left if left else right 

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root, p, q)