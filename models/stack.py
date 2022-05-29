from stack.models.complex import Complex
from stack.models.node import Node


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, el: Complex) -> None:
        if self.head is None:
            self.head = Node(el)
        else:
            new_node = Node(el, self.head)
            self.head = new_node
        self.length += 1

    def push_at_beginning(self, el: Complex) -> None:
        if self.head is None:
            self.head = Node(el)
        else:
            itr = self.head
            index = self.length
            while index-1:
                index -= 1
                itr = itr.next

        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            el_to_pop = self.head.el
            self.head = self.head.next
            self.length -= 1
            return el_to_pop

    def clear(self):
        while self.length > 0:
            self.pop()

    def print(self):
        if self.head is None:
            print("Stack is empty")
        else:
            itr = self.head
            while itr:
                print(itr.el.__repr__())
                itr = itr.next

    def get_length(self):
        return self.length
