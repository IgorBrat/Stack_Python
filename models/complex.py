class Complex:
    def __init__(self, re: int, im: int):
        self.__re = re
        self.__im = im

    def __repr__(self):
        return complex(self.__re, self.__im)
