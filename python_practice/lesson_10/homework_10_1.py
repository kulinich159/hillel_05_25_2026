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
    def __init__(self, team_size, name, salary, department, programming_language):
        self.team_size = team_size
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)

    def __str__(self):
        return (f"Розробник {self.name}, є лідером команди з '{self.team_size}' {self.programming_language} розробників"
                f" в {self.department} департаменті, із зарплатою '{self.salary}'")

list_of_attribute = ["name", "salary", "department", "programming_language", "team_size", "some_new_atr"]

def check_if_attribute_present(obj):
    for element in list_of_attribute:
        if hasattr(obj, element):
            print(f"Атрибут {element} знайдено!")
        else:
            print(f"Атрибут {element} НЕ знайдено!")

print(TeamLead.mro())

teamleader = TeamLead(23, "Alex", 987654, "R&D", "C++")
print(teamleader)

check_if_attribute_present(teamleader)