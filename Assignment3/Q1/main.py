from linkedlist import LinkedList
import random


def main():
    print()
    linked_list = LinkedList()
    linked_list.initialize()
    # Traverse original linked list
    print("Original Linked List(Just traverse):\t", end="")
    linked_list.traverse()
    
    # Traverse Reversed linked list
    print("Reversed Linked List:\t\t\t", end="")
    linked_list.reverse()
    linked_list.traverse()

    # Append random value and traverse the list
    random_value = random.randint(1, 50)
    print("Append", random_value, ":\t\t\t\t", end="")
    linked_list.append(random_value)
    linked_list.traverse()

    # Insert random value and traverse the list
    random_value = random.randint(1, 50)
    random_position = random.randint(1, linked_list.length)
    print("Insert", random_value, "after",
          random_position, "th element:\t\t", end="")
    linked_list.insert(random_value, random_position)
    linked_list.traverse()

    # Remove random position element and traverse the list
    random_position = random.randint(1, linked_list.length)
    print("Remove", random_position, "th element:\t\t\t", end="")
    linked_list.remove(random_position)
    linked_list.traverse()
    print()

if __name__ == "__main__":
    main()
