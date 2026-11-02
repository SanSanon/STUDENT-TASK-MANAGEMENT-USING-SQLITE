from student_repo import StudentRepository
from student_service import StudentService



def main():
    repo = StudentRepository()
    service = StudentService(repo)


    while True:
        print("\n---- STUDENT MANAGEMENT SYSTEM ----")
        print("1. ADD Student\n")
        print("2. View Students\n")
        print("3. Delete Student\n")
        print("4. EXIT\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                student_id = int(input("Enter student id: "))
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                grade = int(input("Enter student grade: "))
                service.add_student(student_id, name, age, grade)
            except ValueError as e:
                print(e)
            else:
                print("Student added successfully!")

        elif choice == "2":
            students = service.get_students()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {(student[2])}, Grade: {(student[3])}")

        elif choice == "3":
            try:
                student_id = int(input("Enter student id: "))
                service.delete_student(student_id)
            except ValueError as e:
                print(e)
            else:
                print(f"Student Id {student_id} was deleted successfully")

        elif choice == "4":
            print("Exiting the system...")
            repo.close()
            break

        else:
            print("Invalid choice. Please try again.")





if __name__ == "__main__":
    main()