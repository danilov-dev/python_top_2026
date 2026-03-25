import sqlite3

# Подключение к базе
conn = sqlite3.connect('school.db')

# Cursor - объект для выполнения запросов
cursor = conn.cursor()

# Создание таблицы учеников
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT NOT NULL,
grade INTEGER CHECK(grade BETWEEN 1 AND 11)
)
''')

# Создание таблицы предметов
cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
)
''')

# Создание таблицы оценки
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER REFERENCES students(id),
subject_id INTEGER REFERENCES subjects(id),
score INTERGER CHECK(score BETWEEN 1 AND 5)
)
''')

# Фиксация изменений в БД
conn.commit()
print("Таблицы созданы")
conn.close()