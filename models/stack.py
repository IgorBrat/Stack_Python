from stack.models.complex import Complex
from stack.models.node import Node


class Stack:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def push(self, el: Complex) -> None:
        if self.__head is None:
            self.__head = Node(el)
        else:
            new_node = Node(el, self.__head)
            self.__head = new_node
        self.__length += 1

    def push_at_beginning(self, el: Complex) -> None:
        if self.__head is None:
            self.__head = Node(el)
        else:
            itr = self.__head
            index = self.__length
            while index-1:
                index -= 1
                itr = itr.next
            itr.next = Node(el)
        self.__length += 1

    def pop(self):
        if self.__head is None:
            return None
        else:
            el_to_pop = self.__head.el
            self.__head = self.__head.next
            self.__length -= 1
            return el_to_pop

    def find_el(self, el: Complex):
        pass

    def clear(self):
        while self.__length > 0:
            self.pop()

    def print(self):
        if self.__head is None:
            print("Stack is empty")
        else:
            itr = self.__head
            while itr:
                print(itr.el.__repr__())
                itr = itr.next

    def get_length(self):
        return self.__length
