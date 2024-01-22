class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.value)

def build_tree(arr, index, n):
    # Base case
    if index < n:
        root = TreeNode(arr[index])
        root.left = build_tree(arr, 2 * index + 1, n)
        root.right = build_tree(arr, 2 * index + 2, n)
        return root
    return None

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

# Create a binary tree using the array [4, 2, 5, 1, 6, 3, 7]
arr = [1, 2, 3, 4, 5, 6, 7]
root = build_tree(arr, 0, len(arr))

# Perform in-order traversal
print("In-order Traversal:")
in_order_traversal(root)
