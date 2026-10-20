# def add_student(self, student_id, name, age, grade):
# check if age is valid (greater than 15)
# check if grade is valid (greater than 70)
# If all valid then create a new Student instance and call the repository layer’s add_student function with this instance.
# def get_students(self): Fetch all students by calling repository layer’s get_students
# def delete_student(self, student_id): Delete the student by calling repository layer’s delete_student

def add_student(self, student_id, name, age, grade):
    cursor.excute("SELECT id FROM Students WHERE (student_id, name, age, grade) = (?,?,?,?)", (author_name,)")