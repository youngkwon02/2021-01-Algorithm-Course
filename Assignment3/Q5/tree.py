from node import Node


class RedBlackTree:
    def __init__(self):
        self.nil = Node(-1)
        self.nil.color = "Black"
        self.root = self.nil

    def pre_order_traversal(self):
        print("Pre-Order Traversal")
        self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, root):
        if root is None:
            pass
        else:
            if root.data != -1:
                print(root.data, "/", root.color)
                self._pre_order_traversal(root.left)
                self._pre_order_traversal(root.right)

    def insert(self, key):
        node = Node(key)
        node.left = self.nil
        node.right = self.nil

        target_node = self.root
        parent_node = None

        while target_node != self.nil:
            parent_node = target_node
            if node.data < target_node.data:
                target_node = target_node.left
            else:
                target_node = target_node.right

        node.parent = parent_node
        if parent_node == None:
            self.root = node
        elif node.data < parent_node.data:
            parent_node.left = node
        else:
            parent_node.right = node

        if node.parent == None: # It means the created node would be the root node
            node.color = "Black"
            return

        if node.parent.parent == None:
            return

        self._fix(node)

    def _fix(self, new_node):
        while new_node.parent.color == "Red":
            if new_node.parent == new_node.parent.parent.right:
                uncle = new_node.parent.parent.left
                if uncle.color == "Red":
                    uncle.color = "Black"
                    new_node.parent.color = "Black"
                    new_node.parent.parent.color = "Red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    new_node.parent.color = "Black"
                    new_node.parent.parent.color = "Red"
                    self.left_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right
                if uncle.color == "Red":
                    uncle.color = "Black"
                    new_node.parent.color = "Black"
                    new_node.parent.parent.color = "Red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    new_node.parent.color = "Black"
                    new_node.parent.parent.color = "Red"
                    self.right_rotate(new_node.parent.parent)
            if new_node == self.root:
                break
        self.root.color = "Black"

    def left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        if temp.left != self.nil:
            temp.left.parent = node

        temp.parent = node.parent
        if node.parent == None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        if temp.right != self.nil:
            temp.right.parent = node

        temp.parent = node.parent
        if node.parent == None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp
