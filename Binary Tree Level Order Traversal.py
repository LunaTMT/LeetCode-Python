from typing import Optional, List, TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []

        res = []
        Q = deque([root])

        while Q:
            n = len(Q)
            currentLevel = []

            for _ in range(n):
                
                node = Q.popleft()
                currentLevel.append(node.val)

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                            
            res.append(currentLevel)
        return res