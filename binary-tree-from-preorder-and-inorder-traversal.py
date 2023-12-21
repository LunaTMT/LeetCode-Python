class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)


    def helper(self, preorder, preStart, preEnd, inorder, inStart, inEnd):

        if preStart > preEnd or inStart > inEnd:
            return None

        rootValue = preorder[preStart]
        root = TreeNode(rootValue)
        
        for i in range(inStart, inEnd + 1): 
            if inorder[i] == rootValue:
                Inorder_root_index = i
                break
                
  
        leftSubtreeSize = Inorder_root_index - inStart
     
        root.left = self.helper(preorder, preStart + 1, preStart + leftSubtreeSize, inorder, inStart, Inorder_root_index - 1)
        root.right = self.helper(preorder, preStart + leftSubtreeSize + 1, preEnd, inorder, Inorder_root_index + 1, inEnd)
        
        return root

#OR
    
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

    return root