# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, current_max):
        if not root:
            return 0
        
        count = 0
        if current_max <= root.val:
            current_max = root.val
            count = 1
        
        left = self.dfs(root.left, current_max)
        right = self.dfs(root.right, current_max)
        
        return left + right + count

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -1 * (10 ** 4))