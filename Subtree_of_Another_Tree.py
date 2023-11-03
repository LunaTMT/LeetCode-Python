def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if not t: return True
    if not s: return False
    if self.isSameTree(s, t): return True

    return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

def isSameTree(self, s, t):
    if not s and not t: return True
    if s and t and s.val == t.val:
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
    return False


"""
OR 

    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False
    
    
    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None

"""