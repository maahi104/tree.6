class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def is_leaf(node):
    return node.left is None and node.right is None

def sum_left_leaves(root):
    if root is None:
        return 0

    sum = 0
    if root.left is not None:
        if is_leaf(root.left):
            sum += root.left.data
        else:
            sum += sum_left_leaves(root.left)

    sum += sum_left_leaves(root.right)

    return sum

# Example usage
if __name__ == '__main__':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("Sum of left leaves: ", sum_left_leaves(root))