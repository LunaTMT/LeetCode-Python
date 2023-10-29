def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:

    if not arr: return None
    q = len(arr)//2

    root = TreeNode(arr[q])
    root.left = self.sortedArrayToBST(arr[:q])
    root.right = self.sortedArrayToBST(arr[q+1:])

    return root

    