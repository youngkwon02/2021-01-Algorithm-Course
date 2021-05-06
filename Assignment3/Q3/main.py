
def input_tree():
    tree_list = [x for x in input("> Input: ").split(', ')]
    for index in range(0, len(tree_list)):
        try:
            tree_list[index] = int(tree_list[index])
        except:
            pass
    return tree_list


def print_invalidation(tree_list, index):
    print("Found invalid part like below!\n------------------------------")
    print("Parent: ", tree_list[index], "\nLeft Child: ",
          tree_list[2*index + 1], "\nRight Child: ", tree_list[2*index + 2])


def is_valid_BST(tree_list):
    length = len(tree_list)
    for index in range(0, length):
        if (2*index + 1) >= length:
            break
        if tree_list[index] == "null" or (tree_list[2*index + 1] == "null" and tree_list[2*index + 2] == "null"):
            continue
        elif tree_list[2*index + 1] == "null":
            if tree_list[index] > tree_list[2*index + 2]:
                print_invalidation(tree_list, index)
                return False
        elif tree_list[2*index + 2] == "null":
            if tree_list[index] < tree_list[2*index + 1]:
                print_invalidation(tree_list, index)
                return False
        if tree_list[index] < tree_list[2*index + 1] or tree_list[index] > tree_list[2*index + 2]:
            print_invalidation(tree_list, index)
            return False
    return True


def main():
    tree_list = input_tree()
    is_valid = is_valid_BST(tree_list)
    print("> Output: ", is_valid)


if __name__ == "__main__":
    main()
