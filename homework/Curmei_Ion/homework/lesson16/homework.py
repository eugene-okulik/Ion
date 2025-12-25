import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()
# connect to database
db = mysql.connect(
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

dotenv.load_dotenv()

# connect to database
db = mysql.connect(
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor(dictionary=True)

# find eugen file
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
ion_path = os.path.dirname(homework_path)
eugen_path = os.path.join(ion_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

# open and read csv file
with open(eugen_path, newline="") as eugen_file:
    reader = csv.reader(eugen_file)
    data = []
    for row in reader:
        data.append(row)

base = []

for row in data:
    (
        name,
        second_name,
        group_title,
        book_title,
        subject_title,
        lesson_title,
        mark_value,
    ) = row

    cursor.execute(
        """
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
        WHERE s.name = %s AND s.second_name = %s
          AND g.title = %s AND b.title = %s
          AND sub.title = %s AND l.title = %s AND m.value = %s
    """,
        (
            name,
            second_name,
            group_title,
            book_title,
            subject_title,
            lesson_title,
            mark_value,
        ),
    )

    result = cursor.fetchone()
    if result:
        base.append(row)

print("Rânduri care există în baza de date:\n")
for r in base:
    print(r)

db.close()
