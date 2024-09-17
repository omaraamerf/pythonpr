import sqlite3
from datetime import date
class Datamanager:
    def __init__(self, db_name="university.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            date_of_birth TEXT,
            date_of_enroll TEXT DEFAULT CURRENT_DATE
        )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS lecturers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            hire_date TEXT,
            department TEXT
        )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            lecturer_id INTEGER,
            FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
        )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade REAL,
            assignment_id INTEGER,
            student_id INTEGER,
            FOREIGN KEY (assignment_id) REFERENCES assignments (id),
            FOREIGN KEY (student_id) REFERENCES students (id)
        )"""
        )

        self.conn.commit()

    def close(self):
        self.conn.close()