from stack.models.complex import Complex
from stack.models.stack import Stack


def main() -> None:
    # key = 0
    # while key != 9:
    #     print(
    #         """Choose option:
    #         1 - Add element to head
    #         2 - Add element to front
    #         3 - Print length of stack
    #         4 - Find position of element
    #         5 - Print stack
    #         6 - Delete head element
    #         7 - Find element by index
    #         8 - Clear stack
    #         9 - End work""")
    #     key = int(input("Your option: "))
    #     match key:
    #         case 1:
    #             pass
    #         case 2:
    #             pass
    #         case 3:
    #             pass
    #         case 4:
    #             pass
    #         case 5:
    #             pass
    #         case 6:
    #             pass
    #         case 7:
    #             pass
    #         case 8:
    #             pass
    stack = Stack()
    stack.push(Complex(2, 3))
    stack.push(Complex(1, 2))
    stack.push(Complex(0, 5))
    stack.print()
    print(f"Size: {stack.get_length()}")
    print("==========")
    stack.push_at_beginning(Complex(4, 4))
    stack.print()
    print(f"Size: {stack.get_length()}")
    print("==========")
    stack.push(Complex(4, 4))
    stack.print()
    print(f"Size: {stack.get_length()}")


if __name__ == "__main__":
    main()
