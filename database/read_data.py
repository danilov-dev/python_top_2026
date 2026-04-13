import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

query_all_students = """
    SELECT *
    FROM students
"""

query_students_high = """
    SELECT name, grade
    FROM students
    WHERE grade >= 9
"""

cursor.execute(query_all_students)
rows = cursor.fetchall()
conn.close()
for row in rows:
    print( f"Student: {row[1]}")