from __future__ import annotations
from stack.models.complex import Complex


class Node:
    """Class to store data of Complex numbers and reference to the next element in stack"""

    def __init__(self, element: Complex = None, next: Node = None):
        self.__element = element
        self.__next = next

    @property
    def element(self):
        return self.__element

    @property
    def next(self):
        return self.__next

    @element.setter
    def element(self, element: Complex):
        self.__element = element

    @next.setter
    def next(self, next: Node):
        self.__next = next
