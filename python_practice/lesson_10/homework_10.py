from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        self.department = department
        super().__init__(name, salary)

class Developer(Employee):
    def __init__(self, name, salary, programming_language = "Python"):
        self.programming_language = programming_language
        super().__init__(name, salary)

class TeamLead(Manager, Developer):
    def __init__(self, team_size, name, salary, department):
        self.team_size = team_size
        Manager.__init__(self, name, salary, department)

    def __str__(self):
        return (f"Розробник {self.name}, є лідером команди з '{self.team_size}' {self.programming_language} розробників"
                f" в {self.department} департаменті, із зарплатою '{self.salary}'")

list_of_attribute = ["name", "salary", "department", "programming_language", "team_size"]

def check_if_attribute_present(obj):
    for element in list_of_attribute:
        if hasattr(obj, element):
            print(f"Атрибут {element} знайдено!")
        else:
            print(f"Атрибут {element} НЕ знайдено!")


teamleader = TeamLead(23, "alex", 10000, "R&D")
print(TeamLead.mro())
print(teamleader)

check_if_attribute_present(teamleader)


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

class Quadrature(Figure):
    def __init__(self, side_length):
        self.side_length = side_length
        self.name = "Квадрат"

    def perimeter(self):
        return 4 * self.side_length

    def square(self):
        return self.side_length**2

class Equilateral_triangle(Figure):
    def __init__(self, side_length):
        self.side_length = side_length
        self.name = "Рівносторонній трикутник"

    def perimeter(self):
        return 3 * self.side_length

    def square(self):
        return (self.side_length**2 * (3**(1/2))) / 4

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Круг"

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def square(self):
        return 3.14 * self.radius**2

quadrature = Quadrature(3)
equilateral_triangle = Equilateral_triangle(6)
circle = Circle(54)

figures = [quadrature , equilateral_triangle, circle]
for figure in figures:
    print(f"{figure.name}: Периметр = {figure.perimeter()}, Площа = {figure.square()}")