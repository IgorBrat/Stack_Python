from stack.models.complex import Complex
from stack.models.node import Node


class Stack:
    """Stack realised on linked list"""
    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, element: Complex) -> None:
        """Add element to the head of stack"""
        if self.__head is None:
            self.__head = Node(element)
        else:
            new_node = Node(element, self.__head)
            self.__head = new_node
        self.__size += 1

    def push_at_beginning(self, element: Complex) -> None:
        """Add element to the beginning of stack"""
        if self.__head is None:
            self.__head = Node(element)
        else:
            itr = self.__head
            index = self.__size
            while index - 1:
                index -= 1
                itr = itr.next
            itr.next = Node(element)
        self.__size += 1

    def pop(self):
        """
        Pop the head element
        :return: Head element
        """
        if self.__head is None:
            return None
        else:
            el_to_pop = self.__head.element
            self.__head = self.__head.next
            self.__size -= 1
            return el_to_pop

    def find_el_pos(self, element: Complex):
        """
        Find position of inputted Complex number
        :param element: Complex number
        :return: its index if this number exists in stack
        """
        if self.__head is None:
            return "Stack is empty"
        else:
            itr = self.__head
            index = self.__size
            while itr:
                if itr.element.__eq__(element):
                    return index
                index -= 1
                itr = itr.next
            return "No such element"

    def find_el_by_index(self, index: int):
        """
        Find Complex number by its index
        :param index: index of searched number
        :return: number if inputted index in range of stack`s size
        """
        if self.__head is None:
            return "Stack is empty"
        elif index > self.__size or index < 1:
            return "Index out of range"
        else:
            itr = self.__head
            pos = self.__size
            while itr:
                if pos == index:
                    return itr.element
                pos -= 1
                itr = itr.next
            return "No such element"

    def clear(self):
        """Clear stack"""
        while self.__size > 0:
            self.pop()

    def print(self):
        """Print all elements of stack from head to beginning"""
        if self.__head is None:
            print("Stack is empty")
        else:
            itr = self.__head
            while itr:
                print(itr.element.__repr__())
                itr = itr.next

    def get_size(self):
        """Get size of stack"""
        return self.__size
