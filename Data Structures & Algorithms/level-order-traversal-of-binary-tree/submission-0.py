# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root):
        queue = deque([root])
        lot = []
        while queue:
            size = len(queue)
            visited = []
            for _ in range(size):
                node = queue.popleft()
                visited.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            lot.append(visited)
        return lot

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        return self.bfs(root)