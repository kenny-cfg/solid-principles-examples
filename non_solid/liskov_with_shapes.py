class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class PerimeterCalculator:
    def calculate(self, rectangle: Rectangle) -> int:
        return 2 * (rectangle.height + rectangle.width)


if __name__ == '__main__':
    square = Square(5)
    calculator = PerimeterCalculator()
    perimeter = calculator.calculate(square)
    print(perimeter)