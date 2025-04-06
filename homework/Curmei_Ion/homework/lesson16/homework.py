from tkinter.font import names

import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()
# connect to database
db = mysql.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

# find eugen file
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
ion_path = os.path.dirname(homework_path)
eugen_path = os.path.join(ion_path, 'eugene_okulik\\Lesson_16\\hw_data', 'data.csv')

# open and read csv file
with open(eugen_path, newline='') as eugen_file:
    reader = csv.reader(eugen_file)
    data = []
    for row in reader:
        data.append(row)

for row in data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
    # print(name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)

cursor.execute("select * from students")
rezult = cursor.fetchall()
db_name = []
db_second_name = []

for row in rezult:
    db_name.append(row['name'])
    db_second_name.append(row['second_name'])

base = [name for name in db_name if name in data]
print(f"Name what exist in data base is: {base}")
db.close()
