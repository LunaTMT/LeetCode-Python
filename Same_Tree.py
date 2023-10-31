def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)