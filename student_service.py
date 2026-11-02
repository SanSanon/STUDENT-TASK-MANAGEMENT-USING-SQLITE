
from student import Student

class StudentService:
    def __init__(self, repo):
        self.repo = repo
  
    def add_student(self, student_id, name, age, grade):
        if age <= 15:
            raise ValueError("Age must be greater than 15") 
        if grade <= 70:
            raise ValueError("Grade must be greater than 70")
        
        student = Student(student_id, name, age, grade)
        self.repo.add_student(student)


    def get_students(self):
        students = self.repo.get_students()
        return students

    def delete_student(self, student_id):
        self.repo.delete_student(student_id)

  
