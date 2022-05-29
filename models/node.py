from __future__ import annotations
from stack.models.complex import Complex


class Node:
    def __init__(self, el: Complex = None, next: Node = None):
        self.el = el
        self.next = next
