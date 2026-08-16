import random
import time

from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from faker import Faker

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
DATABASE_URL = "postgresql://postgres:O_gurec145@127.0.0.1/test_db"
engine = create_engine(DATABASE_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()

# Визначення моделі даних (таблиці) за допомогою класу
class ORMUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return  f"id={self.id}, name={self.name}, age={self.age}"

# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Додавання користувачів до бази даних
# session.add_all([
#     User(name='John', age=30),
#     User(name='Alice', age=25),
#     User(name='Bob', age=35),
# ])
# session.commit()
# SQL аналог:
# INSERT INTO users (name, age) VALUES ('John', 30), ('Alice', 25), ('Bob', 35);

# Використання виразів для складного запиту: обчислення середнього віку користувачів
average_age = session.query(func.avg(ORMUser.age)).scalar()
print("Середній вік користувачів:", average_age)
# SQL аналог: SELECT AVG(age) FROM users;

# Використання виразів для складного запиту: підрахунок кількості користувачів
user_count = session.query(func.count(ORMUser.id)).scalar()
print("Кількість користувачів:", user_count)

# Використання виразів для складного запиту: підрахунок кількості користувачів
user_count = session.query(func.count(ORMUser.id)).first()
print("Кількість користувачів:", user_count)

print("----------------------:")
user_less_40 = session.query(ORMUser).filter(ORMUser.age < 40).all()
print(*user_less_40, sep='\n')
print("--------------------")
# SQL аналог: SELECT COUNT(id) FROM users;

# апдейт значеня
# user = session.query(ORMUser).filter_by(name='John').first()
# user.age = 99
# видалення значеня
# user_13 = session.query(ORMUser).filter_by(id=13).first()
# session.delete(user_13)

faker = Faker()

# for k in range(5):
#     session.add(ORMUser(name=f"{faker.name()}-{time.time()}", age=random.randint(18, 100)))


retired_user = session.query(ORMUser).filter(ORMUser.age > 60).all()

for k in retired_user:
    session.delete(k)

session.commit()

all_users = session.query(ORMUser).all()
print(*all_users, sep='\n')
print(all_users[5].name)
# Закриття сесії
session.close()