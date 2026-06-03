
students = [('Alice', 88), ('Bob', 75), ('Carol', 96)]

def get_grade(student):
    return student[1]

students.sort(key=get_grade)
print(students)