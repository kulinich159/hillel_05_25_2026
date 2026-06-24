print("---------------------------lambda function------------------------")

def count_h(word):
    return word.count("h")

print(id(count_h))

new_fn = count_h

print(count_h("hello"))
print(new_fn("hello"))
print(type(new_fn))
print(id(new_fn))


print(max([1,2,3,4]))
print(max(["hhh", "Hello", ''], key=count_h))
print(max(["hhh", "Hello", ''], key=lambda  x:x.count("h")))

new_lambda = lambda x,y:pow(x, y)
print(new_lambda(2,5))

print("---------------------------Class example------------------------")

class Car:

    class_name = "Car class"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.tank = 0

    def set_tank(self, value): # class method
        self.tank = value

    def go_somewhere(self, amount_in_km):
        if self.tank >= amount_in_km:
            self.tank = self.tank - amount_in_km
            print("Driving...")
        else:
            print("Can't go - have not enough fuel")

x5 = Car(brand="BMW", model="X5") # instance
print(x5.brand)
print(x5.model)

polo = Car(brand="VW", model="Polo") # instance
print(polo.brand)
print(polo.model)
polo.tank = 50
print(polo.tank)

polo.set_tank(100)
print(polo.tank)

print(x5.tank)

print("---------------------------User Class------------------------")
class User:
    def __init__(self, name, password, site_url): #constructor
        self.name = name
        self.password = password
        self.url = site_url

    def login(self):
        print(f"User {self.name} was logged in {self.url}")

    def logout(self):
        print(f"User {self.name} was logged out {self.url}")


dev_user = User("dev_ser", "dev_password", "https://dev-example.com/" ) # instance creation

print(dev_user.name) #attribute
dev_user.login() #method
dev_user.logout() #method

stage_user = User("stage_ser", "stage_password", "https://stage-example.com/" )
prod_user = User("prod_ser", "prod_password", "https://prod-example.com/" )

print("---------------------------Animal Class------------------------")

class Animal:
    def make_sound(self):
        print("Animal sound")

    def make_sleep(self):
        print("Sleeping...")

    # def dog_sound(self):
    #     print("Grr")
    #
    # def cat_sound(self):
    #     print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Grr")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bug(Animal):
    pass

dog = Dog()
cat = Cat()
unknown_animal = Animal()
bug = Bug()


dog.make_sound()
cat.make_sound()
unknown_animal.make_sound()
bug.make_sound()

dog.make_sleep()
cat.make_sleep()

print("---------------------------Encapsulation------------------------")

x5.set_tank(50)
x5.go_somewhere(40)
x5.go_somewhere(40)
polo.set_tank(30)
polo.go_somewhere(40)

print("---------------------------Self example------------------------")

class Auto:
    def __init__(self, model, color, engine, fuel_to_km=0.2):
        self.model = model
        self.color = color
        self.engine = engine
        self.tank = 0
        self.__fuel_to_km = fuel_to_km

    def drive_to_nearest_town(self, distance_km):
        if self.tank / self.__fuel_to_km >= distance_km:
            self.tank = self.tank - distance_km* self.__fuel_to_km
            print("Driving...")
        else:
            print(f"Can't go there, have fuel only on {self.tank/self.__fuel_to_km} km")


class Nissan(Auto):
    brand = "Nissan"

    @classmethod
    def say_greeting(cls):
        print(f"Hello from {cls.brand}")

y61 = Nissan(model="y61", color="green", engine="3.0")
navaro = Nissan(model="navaro", color="red", engine="5.0")

print(y61.model)
print(navaro.model)
y61.tank = 50
y61.drive_to_nearest_town(400)
y61.drive_to_nearest_town(400)
navaro.tank = 10
navaro.drive_to_nearest_town(300)
# Nissan.brand = "New Nissan"
# navaro.__class__.brand = "New Nissan"
print(navaro.brand)
print(y61.brand)

y61.say_greeting()
navaro.say_greeting()

print("---------------------------Super method------------------------")

class Vehicle:
    def __init__(self, color):
        self.color = color

class Car(Vehicle):
    def __init__(self, color, model, wheels):
        super().__init__(color)
        self.model = model
        self.wheels = wheels

my_car = Car(color="Blue", model="Honda", wheels=4)
print(my_car.wheels)  # Виведе "4"