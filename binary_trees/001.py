class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# class BinaryTree:
#     def __init__(self, root):
#         self.root = Node(root)
#
#
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.left.left.left = Node(8)


def build_tree(root):
    data = int(input("Enter the data:"))
    root = Node(data)

    if data == -1:
        return None

    print("Enter data for inserting in left of", data)
    root.left = build_tree(root.left)
    print("Enter data for inserting in right of:", data)
    root.right = build_tree(root.right)
    return root


root = None
build_tree(root)
