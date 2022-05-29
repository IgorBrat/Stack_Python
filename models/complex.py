from __future__ import annotations


class Complex:
    def __init__(self, re: int, im: int):
        self.__re = re
        self.__im = im

    def __repr__(self):
        return complex(self.__re, self.__im)

    def __eq__(self, other: Complex):
        condition = (self.__re == other.__re and self.__im == other.__im)
        return condition
