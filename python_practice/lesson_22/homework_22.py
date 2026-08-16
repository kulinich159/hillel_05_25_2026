import random
from sqlalchemy import create_engine, Column, Integer, String, func, ForeignKey, Table, select
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from faker import Faker

faker = Faker()
DATABASE_URL = "postgresql://postgres:omnom-moniom@127.0.0.1/test_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("StudentCourses", back_populates="students")

    def __str__(self):
        return f"id={self.id}, name={self.name}"

class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("StudentCourses", back_populates="courses")

    def __str__(self):
        return  f"id={self.id}, name={self.name}"


class StudentCourses(Base):
    __tablename__ = "student_courses"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)

    students = relationship("Students", back_populates="courses")
    courses = relationship("Courses", back_populates="students")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Створення 5 записів в базі з курсами
courses_list = ["Python" ,"SQL", "Algorithms","Docker", "Testing"]
for k in courses_list:
     session.add(Courses(name=k))

# Створення 20 записів в базі з студентами
for k in range(20):
    session.add(Students(name=f"{faker.name()}"))

courses_ids_list = [course.id for course in session.query(Courses).all()]
students_ids_list  = [student.id for student in session.query(Students).all()]

# Додаємо для студентів рандомний курс
for student in students_ids_list:
    session.add(StudentCourses(student_id=student, course_id=random.sample(courses_ids_list)))

result_of_join_data = (session.query(Students.name, Courses.name).join(StudentCourses, Students.id == StudentCourses.student_id)
    .join(Courses, Courses.id == StudentCourses.course_id).all())

for student_name, course_name in result_of_join_data:
    print(f"{student_name},  проходить курс - {course_name}")

# Додати нового студента
session.add(Students(name="Test"))

# Апдейт студента
student_update = session.query(Students).filter_by(name='Test').first()
student_update.name = "Testoria"

# Видалення студента
student_delete = session.query(Students).filter_by(name="Testoria").first()
session.delete(student_delete)

session.commit()
session.close()