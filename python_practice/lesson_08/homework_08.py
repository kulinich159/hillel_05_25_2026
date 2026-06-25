class Student:
    def __init__(self, first_name, second_name, age, avg_score=0):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.avg_score = avg_score

    def change_student_avg_score(self, value):
        self.avg_score = value

student = Student(first_name="Степан", second_name="Банах", age=17)
student.change_student_avg_score(56)

print(f"Ім'я: {student.first_name}, Прізвище: {student.second_name}, Вік: {student.age} років, Середній бал: {student.avg_score}")
