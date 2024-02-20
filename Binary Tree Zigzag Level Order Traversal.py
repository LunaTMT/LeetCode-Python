class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.value)

def levels_of_binary_tree(root):
    if not root:
        return []

    res = []
    queue = [(root, 0)]

    while queue:
        node, level = queue.pop()

        if len(res) <= level:
            res.append([])
        
        res[level].append(node.value)

        if node.left:
            queue.append((node.left, level+1))

        if node.right:
            queue.append((node.right, level+1))

    for i in range(2, len(res), 2):
        res[i].reverse()
    
    return res


# Given list
input_list = [3, 9, 20, None, None, 15, 7]

# Create TreeNode objects
nodes = [TreeNode(val) if val is not None else None for val in input_list]

# Set the relationships between nodes
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]

levels_of_binary_tree(root)