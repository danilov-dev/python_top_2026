import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

students = [
    ('Алексей Петров', 'alex@mail.ru', 10),
    ('Мария Иванова', 'maria@mail.ru', 10),
    ('Сергей Владимиров', 'serge@mail.ru', 9),
    ('Галина Кравцова', 'galina@mail.ru', 9),
    ('Светлана Иванова', 'svetlana@mail.ru', 2),
    ('Петр Сидоров', 'petr@mail.ru', 3),
]

cursor.executemany("INSERT INTO students(name, email, grade) VALUES (?, ?, ?)", students)
conn.commit()
print('Данные о студентах успешно добавлены!')
conn.close()
