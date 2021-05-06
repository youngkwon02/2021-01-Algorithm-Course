from tree import RedBlackTree


def main():
    rbt = RedBlackTree()
    rbt.insert(41)
    rbt.insert(38)
    rbt.insert(31)
    rbt.insert(12)
    rbt.insert(19)
    rbt.insert(8)
    rbt.pre_order_traversal()


if __name__ == "__main__":
    main()
