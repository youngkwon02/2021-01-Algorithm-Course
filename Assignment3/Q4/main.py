from tree import Tree


def main():
    tree = Tree()
    for i in range(0, 3):
        a, b = input("> Input: ").split(", ")
        tree.get_lowest_common_ancestor(int(a), int(b))


if __name__ == "__main__":
    main()