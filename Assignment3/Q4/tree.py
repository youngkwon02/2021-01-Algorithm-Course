from tree_node import TreeNode


class Tree:
    def __init__(self):
        self.root = TreeNode(6)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(8)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(9)

    def get_path_to_element(self, parent, element, path=[]):
        # Call this function as get_path_to_element(Tree.root, target, [])
        path.append(parent.data)
        if element == parent.data:
            return path
        elif element < parent.data:
            self.get_path_to_element(parent.left, element, path)
        else:
            self.get_path_to_element(parent.right, element, path)

    def get_lowest_common_ancestor(self, a, b):
        path_a = []
        path_b = []
        self.get_path_to_element(self.root, a, path_a)
        self.get_path_to_element(self.root, b, path_b)
        path_a_as_set = set(path_a)
        common = path_a_as_set.intersection(path_b)
        common_ancestor = list(common)
        print("> Output: ", min(common_ancestor))
