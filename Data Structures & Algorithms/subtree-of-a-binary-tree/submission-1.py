# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialization(sef, root):
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    
    def compare(self, lps, tree, subtree):
        i = 0
        j = 0
        n = len(tree)
        m = len(subtree)
        while i < n:
            if tree[i] == subtree[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                if j != 0:
                    j = lps[j  - 1]
                else:
                    i += 1
        return False
       
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = self.serialization(root)
        subtree = self.serialization(subRoot)
        m = len(subtree)
        lps = [0 for _ in range(m)]
        i = 1
        l = 0
        while (i < m):
            if (subtree[i] == subtree[l]):
                l += 1
                lps[i] = l
                i += 1
            else:
                if (l != 0):
                    l = lps[l - 1]
                else:
                    i += 1
        return self.compare(lps, tree, subtree)