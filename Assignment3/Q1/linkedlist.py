from node import Node
import random


class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.tail = self.head
        self.current = None
        self.length = 0

    def initialize(self):
        for index in range(0, 10):
            random_value = random.randint(1, 50)
            self.append(random_value)

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def insert(self, data, after_nth_element):
        if after_nth_element >= self.length:
            self.append(data)
        else:
            new_node = Node(data)
            self.current = self.head
            for index in range(0, after_nth_element):
                self.current = self.current.next
            new_node.next = self.current.next
            self.current.next = new_node
            self.length += 1

    def traverse(self):
        self.current = self.head
        while True:
            if self.tail == self.current or self.current.next == None:
                break
            self.current = self.current.next
            print(self.current.data, end=" ")
        print()

    def remove(self, after_nth_element):
        if after_nth_element < self.length:
            self.current = self.head
            for index in range(0, after_nth_element-1):
                self.current = self.current.next
            self.current.next = self.current.next.next

    def swap_head_tail(self):
        self.head.next, self.tail = self.tail, self.head.next

    def reverse_recursive(self, current_node):
        if self.tail != current_node.next:
            self.reverse_recursive(current_node.next)
        current_node.next.next = current_node

    def reverse(self):
        self.reverse_recursive(self.head)
        self.swap_head_tail()
