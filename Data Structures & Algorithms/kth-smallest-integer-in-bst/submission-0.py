# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, traversal, k):
        if not root:
            return None
        
        left = self.dfs(root.left, traversal, k)
        if left is not None:
            return left

        traversal.append(root.val)
        if len(traversal) == k:
            return traversal[k - 1]

        right = self.dfs(root.right, traversal, k)
        if right is not None:
            return right
        
        return None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, [], k)