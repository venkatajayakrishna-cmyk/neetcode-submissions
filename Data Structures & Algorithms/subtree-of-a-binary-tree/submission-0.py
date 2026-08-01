# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isIdentical(self, t, s):
        if not t and not s:
            return True
        
        if not t or not s:
            return False
        
        return (
                t.val == s.val 
                and self.isIdentical(t.left, s.left) 
                and self.isIdentical(t.right, s.right)
        ) 

    def dfs(self, root, subRoot):
        if not root:
            return False

        current = self.isIdentical(root, subRoot)
        left = self.dfs(root.left, subRoot)
        right = self.dfs(root.right, subRoot)

        return left or right or current
       
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)