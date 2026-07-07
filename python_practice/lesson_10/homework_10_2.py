from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

class Quadrature(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def perimeter(self):
        return 4 * self.__side_length

    def square(self):
        return self.__side_length**2

class Equilateral_triangle(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def perimeter(self):
        return 3 * self.__side_length

    def square(self):
        return (self.__side_length**2 * (3**(1/2))) / 4

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.__radius

    def square(self):
        return 3.14 * self.__radius**2

quadrature = Quadrature(3)
equilateral_triangle = Equilateral_triangle(6)
circle = Circle(54)

figures = [quadrature , equilateral_triangle, circle]
for figure in figures:
    print(f"{figure.__class__.__name__}: Периметр = {figure.perimeter()}, Площа = {figure.square()}")