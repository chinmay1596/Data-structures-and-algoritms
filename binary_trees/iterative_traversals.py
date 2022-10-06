from stacks.custom_stack import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root)
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root)
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, "")

    def preorder_print(self, root):
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



    def inorder_print(self, root):
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

    def postorder_print(self, start, traversal):
        """
                left -> right -> root
                :param start:
                :param traversal:
                :return:
                """

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


print(tree.print_tree('inorder'))
