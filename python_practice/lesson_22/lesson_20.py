import psycopg2

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = 'test_db'
user = 'postgres'
password = 'O_gurec145'
host = '127.0.0.1'
port = '5432'

# Спроба підключитись до бази даних
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()

    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    cursor.execute("SELECT * from products")

    # Отримання результатів запиту
    record = cursor.fetchone()
    print(record)
    cursor.execute("Select * from products where id = '01a009fa-fe86-7bc8-86f2-36ed87d530fc'")
    record = cursor.fetchall()
    print(record)
    # for _ in record:
    #     print(record)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")