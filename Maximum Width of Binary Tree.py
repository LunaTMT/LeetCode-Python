def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
        return

    queue = deque()
    queue.append(root)
    res = 0

    while queue:
        level_size = len(queue)
        level = []

        for i in range(level_size):
            cur = queue.popleft()
            level.append(cur.val)   

            if cur.left:
                cur.left.val = cur.val * 2
                queue.append(cur.left)
                
            if cur.right:
                cur.right.val = (cur.val * 2) + 1
                queue.append(cur.right)
        res = max(res, level[-1] - level[0] + 1)
    return res