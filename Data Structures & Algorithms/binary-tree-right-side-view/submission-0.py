# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root):
        queue = deque([root])
        visited = []
        while queue:
            size = len(queue)

            node = None
            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            visited.append(node.val)
        return visited

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.bfs(root)