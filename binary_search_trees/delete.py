
from .search import find_node_in_bst


def max_val(root):
    temp = root
    if temp is None:
        return -1

    while temp.right is not None:
        temp = temp.right

    return temp.data


def delete_node_in_bst(root, target):
    if not root:
        return root
    
    # find karo target ko bst me
    if root.data == target:
        if not root.left and not root.right:
            del root
            return None
        
        elif not root.right and root.left:
            child = root.left
            del root
            return child
        
        elif not root.left and root.right:
            child = root.right
            del root
            return child
        
        else:
            # dono child exist karte hai
            # inorder predecessor of left subtree -> left subtree me max value
            predecessor = max_val(root.left)
            root.data = predecessor
            root.left = delete_node_in_bst(root.left, predecessor)
            return root

    elif target > root.data:
        root.right = delete_node_in_bst(root.right, target)
    
    elif target < root.data:
        root.left = delete_node_in_bst(root.left, target)
    
    return root