
def find_node_in_bst(root, target):
    if not root:
        return False

    if root.data == target:
        return True

    if target > root.data:
        return find_node_in_bst(root.right, target)
    else:
        return find_node_in_bst(root.left, target)