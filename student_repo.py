from student import Student
import sqlite3

class StudentRepository:
    def __init__(self):
        self.conn = sqlite3.connect("student_library.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(""" 
                        CREATE TABLE IF NOT EXISTS Students (
                        student_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        grade INTEGER NOT NULL
                        )
                        """)
        self.conn.commit()

    def add_student(self, student):
        try:
            self.cursor.execute("INSERT INTO Students (name, age, grade, student_id) VALUES (?, ?, ?, ?)", (student.name, student.age, student.grade, student.student_id))
        except sqlite3.IntegrityError:
            raise ValueError("Student ID already exists")

        self.conn.commit()

    def get_students(self):
        self.cursor.execute("""
            SELECT Students.student_id, Students.name, Students.age, Students.grade
            FROM Students ORDER by student_id
            """)

        students = self.cursor.fetchall()
        return students

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM Students WHERE student_id = ?", (student_id,))
        if self.cursor.rowcount == 0:
            raise ValueError("Student not found")
        self.conn.commit()

    def close(self):
        self.conn.close()