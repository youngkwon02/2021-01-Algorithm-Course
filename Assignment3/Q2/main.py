from linkedlist import LinkedList


def main():
    linked_list = LinkedList()
    linked_list.initialize()

    print("Original Linked list: ", end="")
    linked_list.traverse()
    linked_list.remove_dup()
    print("Duplication removed: ", end="")
    linked_list.traverse()


if __name__ == "__main__":
    main()
