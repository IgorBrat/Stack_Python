from stack.models.complex import Complex
from stack.models.stack import Stack


def main() -> None:
    key = 0
    stack = Stack()
    while key != 9:
        print(
            """Choose option:
            1 - Add element to head
            2 - Add element to front
            3 - Print size of stack 
            4 - Print stack
            5 - Delete head element
            6 - Find position of element
            7 - Find element by index
            8 - Clear stack
            9 - End work""")
        key = int(input("Your option: "))
        match key:
            case 1:
                re = int(input("Input real coordinate: "))
                im = int(input("Input imaginary coordinate: "))
                stack.push(Complex(re, im))
            case 2:
                re = int(input("Input real coordinate: "))
                im = int(input("Input imaginary coordinate: "))
                stack.push_at_beginning(Complex(re, im))
            case 3:
                print(f"Size of stack: {stack.get_size()}")
            case 4:
                stack.print()
            case 5:
                result = stack.pop()
                if result is None:
                    print("Stack is empty")
                else:
                    print(f"Popped element: {result.__repr__()}")
            case 6:
                re = int(input("Input real coordinate: "))
                im = int(input("Input imaginary coordinate: "))
                result = stack.find_el_pos(Complex(re, im))
                if isinstance(result, int):
                    print(f"Position of that element is {result}")
                else:
                    print(result)
            case 7:
                index = int(input("Input index: "))
                result = stack.find_el_by_index(index)
                if isinstance(result, Complex):
                    print(result.__repr__())
                else:
                    print(result)
            case 8:
                stack.clear()


if __name__ == "__main__":
    main()
