from stacks.custom_stack import Stack


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


def preorder_print(root):
    """
    Root -> left -> right
    :param start:
    :param traversal:
    :return:
    """
    if root is None:
        return

    stack = Stack()
    stack.push(root)
    traversal = ""
    while len(stack) > 0:
        node = stack.pop()
        traversal += str(node.data) + "-"

        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)
    return traversal


def inorder_print(root):
    """
    left -> Root-> right
    :param start:
    :param traversal:
    :return:
    """
    current = root
    stack = Stack()
    traversal = ""
    while True:
        if current is not None:
            stack.push(current)
            current = current.left
        elif stack:
            current = stack.pop()
            traversal += str(current.data) + "-"

            current = current.right
        else:
            break

    return traversal


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    else:
        root.right = insert(root.right, data)

    return root


# Function to construct a BST from given keys
def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root


if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]

    root = constructBST(keys)
    print(inorder_print(root))
