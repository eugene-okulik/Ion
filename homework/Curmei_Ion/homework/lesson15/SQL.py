import mysql.connector as mysql

# Conectarea la baza de date
db = mysql.connect(
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students(name, second_name) VALUES ('Automation', 'Programist')")
student_id = cursor.lastrowid

query = "INSERT INTO books(title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('Automation with Python', student_id),
    ('Automation with Java', student_id)
]
cursor.executemany(query, values)

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('api automation', '2025-02-01', '2025-07-31')"
)
group_id = cursor.lastrowid

cursor.execute(f"insert into students(group_id) values ('{group_id}')")

cursor.execute("INSERT INTO subjets (title) VALUES ('front end automation')")
subject_id1 = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('back end automation')")
subject_id2 = cursor.lastrowid

cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('history of automation', '{subject_id1}')")
lesson1_id1 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('base of frontend automation', '{subject_id1}')")
lesson2_id1 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('base of backend automation', '{subject_id2}')")
lesson1_id2 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('advance of backend automation', '{subject_id2}')")
lesson2_id2 = cursor.lastrowid

notes = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
mark = [
    (8, lesson1_id1, student_id),
    (9, lesson2_id1, student_id),
    (9, lesson1_id2, student_id),
    (10, lesson2_id2, student_id)
]
cursor.executemany(notes, mark)
# select all from create students
student_query = f"""
SELECT
    s.id AS student_id,
    s.name,
    s.second_name,
    g.title AS group_name,
    g.start_date,
    g.end_date,
    m.value AS mark,
    l.title AS lesson_title,
    sub.title AS subjets_title,
    b.title AS book_title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = '{student_id}';
"""

cursor.execute(student_query)
student_info = cursor.fetchall()

db.commit()
db.close()
