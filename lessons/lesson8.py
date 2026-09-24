import sqlite3

connect = sqlite3.connect("user_grade.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL)
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR (20) NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id))
''')

connect.commit()

def create_moke_students():
    cursor.executemany('''
        'INSERT INTO 
    ''')

def get_student_grade():

    cursor.execute('''
        SELECT students
    ''')