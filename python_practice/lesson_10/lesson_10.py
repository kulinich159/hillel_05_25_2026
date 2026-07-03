from abc import ABC, abstractmethod


class Train:
    def __init__(self):
        self.locomotive = Wagon(is_locomotive=True, number=1)
        self.wagons = []

    def __len__(self):
        return len(self.wagons)

    def add_wagon(self, wagon: Wagon):
        if wagon.number not in [k.number for k in self.wagons]:
            # wagon = Wagon(is_locomotive=False, number=number)
            self.wagons.append(wagon)

    def __str__(self):
        return f"Train with {len(self.wagons)}: {', '.join([str(k) for k in self.wagons])}"

class Wagon:
    def __init__(self, number, is_locomotive=False):
        self.is_locomotive = is_locomotive
        self.number = number
        self.passenger = []

    def __len__(self):
        return len(self.passenger)

    def __str__(self):
        return f"Wagon # {self.number} with {len(self.passenger)}  {self.passenger}passengers, where locomotive {self.is_locomotive}"

    def add_passenger(self, passenger: dict):
        if len(self.passenger) != 10:
            self.passenger.append(passenger)
        pass



train = Train()

print(train)
wg1 = Wagon(number=2)
wg1.add_passenger({"name": "Alex","pass_num": "23" })
wg1.add_passenger({"name": "Alex1","pass_num": "231" })
print(train)
train.add_wagon(wg1)
print(train)
print(wg1)
print("------------------------------------------MRO-------------------------------------")
class Animal:
    def make_sound(self):
        print("Animal sound")

    def walk(self):
        print("walking.,...")

    def __str__(self):
        return "Animal object"

class Lion(Animal):
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def make_sound(self):
        print("Rrrrrrr")


class Bird(Animal):
    def __init__(self, name):
        self.name = name
        self.wings = 2

    def make_sound(self):
        print("Chiric")

class Hymera(Lion, Bird):
    def __init__(self, name):
        self.name = name
        Lion.__init__(self,name)
        Bird.__init__(self,name)

pushok = Hymera("Pushok")
print(pushok.legs)
print(pushok.wings)
print(pushok.legs)
pushok.make_sound()
print(Hymera.mro())

print("------------------------------------------Abstraction-------------------------------------")

class Tree(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Tree):
    def make_sound(self):
        print("Gavvv")

dog = Dog("Body")
dog.make_sound()

print("------------------------------------------Variable_visibility_area-------------------------------------")
# global
# local
# non local
# build in function

dog_name = "Richi" # global

def doc_actions(name):
    dog_name = name  # on local

    def make_sound():
        dog_name = "naida" # local
        print(dog_name)

    make_sound()
    print(dog_name)


doc_actions("Jack")
print(dog_name)
