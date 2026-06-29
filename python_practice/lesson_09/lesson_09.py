print("---------------------------STR example------------------------")

class User:
    def __init__(self, name, password, site_url, height, score): #constructor
        self.name = name
        self.password = password
        self.site_url = site_url
        self.finished_courses = []
        self.height = height
        if 100 >= score >= 0:
            self.score = score
        else:
            print("score must be between 0 and 100. Set 0")
            self.score = 0

    def __str__(self):
        return f"User: {self.name}, url {self.site_url}, score {self.score}"

    def __repr__(self):
        return f"User='{self.name}', password='{self.password}', url='{self.site_url}'"

    def __len__(self):
        return len(self.finished_courses)

    def __len__(self):
        return self.height

    def __eq__(self, other):
        if isinstance(other, User):
            return self.height == other.height
        return  False

    def __gt__(self, other):
        if isinstance(other, User):
            return self.height > other.height
        return False

    def __ge__(self, other):
        if isinstance(other, User):
            return self.height > other.height
        return False

    def __setattr__(self, key, value):
        if key == 'score':
            if not (100 >= value >= 0):
                print("score must be between 0 and 100. Set 0")
                value =0
        super().__setattr__(key, value)


user_alex = User("Alex", 1234, "example.com", 150, 45)
user_den = User("Den", 1234, "example.com", 158, 56)
print(user_alex)

print(repr(user_alex))

# import logging
# logging.error(repr(user_alex))

user_alex.finished_courses.append("math")
user_alex.finished_courses.append("math1")

print(len(user_alex))
print(user_alex == user_den)
print(user_alex > user_den)
print(user_alex < user_den)

print(user_alex)
user_alex.score = -50
print(user_alex)
print("---------------------------add example------------------------")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

# Використання оператора додавання та автоматичний виклик __add__
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print(result.x, result.y)  # Виведе: 4 6

# class Classes:
#     def __init__(self, **kwargs):
#         for k,v in kwargs.items():
#             setattr(self, k, v)
#
#     def __add__(self, other):
#         for k,v in other.__dict__.items():
#             setattr(self, k, v)
#
#
#     def __str__(self):
#         result = f"current classes\n"
#
#         for k,v in self.__dict__.items():
#             result += f"{k} has students: {v['students']}, start at {v['start']}\n"
#             setattr(self, k,v)
#         return result
#
# class1 = Classes({"name": "John", "name1": "John1"})
#
# print(class1)