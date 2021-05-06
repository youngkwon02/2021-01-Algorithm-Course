from node import Node
import random


class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.tail = self.head
        self.current = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def traverse(self):
        self.current = self.head
        while True:
            if self.tail == self.current or self.current.next == None:
                break
            self.current = self.current.next
            print(self.current.data, end=" ")
        print()

    def initialize(self):
        for index in range(0, 20):
            random_value = random.randint(1, 50)
            self.append(random_value)
            self.length += 1

    def remove_dup(self):
        self.current = self.head
        prev = self.head
        list = []
        while True:
            if self.current.next == None:
                break
            if prev.next != self.current.next:
                prev = self.current
            self.current = self.current.next
            if self.current.data not in list: # Check duplicate numbers
                list.append(self.current.data)
            else:
                prev.next = self.current.next
