from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

            """Basic BFS traversal"""
            
            if not root:
                return []

            res = []
            queue = deque([root])

            while queue:
                level_len = len(queue)
                for i in range(level_len):
                    node = queue.popleft()

                    if i == level_len - 1:
                        res.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            return res
