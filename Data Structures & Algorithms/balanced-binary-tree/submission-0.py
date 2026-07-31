# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def dfs(self, root):
        if not root:
            return 0
        
        leftHeight = self.dfs(root.left) + 1
        rightHeight = self.dfs(root.right) + 1

        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
            return -1
        return max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            self.dfs(root)
        return self.balanced