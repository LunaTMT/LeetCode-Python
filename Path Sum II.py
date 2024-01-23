
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        
        def dfs(node, path, acc):
            if node is None: 
                return

            path.append(node.val)
            acc += node.val

            if node.left is None and node.right is None and acc == target:
                res.append(path.copy())  # Append a copy of the path to avoid modification issues
            
            dfs(node.left, path, acc)
            dfs(node.right, path, acc)

            path.pop()

        res = []
        dfs(root, [], 0)
        return res


