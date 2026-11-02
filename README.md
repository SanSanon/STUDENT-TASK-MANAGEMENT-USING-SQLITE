# Student Management System (SMS)

A Python-based Student Management System built using **Layered Architecture** and **SQLite**. This project demonstrates object-oriented programming (OOP), separation of concerns, database management, and exception handling.

## Features

- **Add Students:** Register students with an ID, name, age, and grade.
- **View Students:** Display all student records stored in the database.
- **Delete Students:** Remove students using their unique student ID.
- **Input Validation:** Ensure students are older than 15 and have grades greater than 70.
- **Duplicate ID Handling:** Prevent students from being registered with an existing student ID.
- **Error Handling:** Handle invalid inputs and nonexistent student records.
- **Persistent Storage:** Store student records in an SQLite database.

## Technologies Used

- **Python 3** — Application development
- **SQLite3** — Relational database management
- **SQL** — Database operations
- **Object-Oriented Programming (OOP)** — Class-based application design

## Project Structure

```text
Student-Management-System/
├── student.py
├── student_repo.py
├── student_service.py
├── main.py
└── README.md
```

## Architecture

The application follows a three-layer architecture to separate responsibilities and improve maintainability.

### 1. Presentation Layer (`main.py`)
Provides a command-line interface (CLI) where users can add, view, and delete student records. It also handles user input and displays error messages.

### 2. Business Logic Layer (`student_service.py`)
Validates student information before processing requests and communicates with the Repository Layer.

Business rules:
- Student age must be greater than 15.
- Student grade must be greater than 70.

### 3. Data Access Layer (`student_repo.py`)
Manages the SQLite database connection and performs SQL operations, including inserting, retrieving, and deleting student records.

### Student Model (`student.py`)
Defines the `Student` class with four attributes:
- `student_id`
- `name`
- `age`
- `grade`

### Application Flow

```text
User
  |
  v
Presentation Layer (main.py)
  |
  v
Business Logic Layer (student_service.py)
  |
  v
Data Access Layer (student_repo.py)
  |
  v
SQLite Database
```

## Getting Started

### Prerequisites

- Python 3 installed
- No external Python packages required; SQLite3 is included with standard Python distributions.

### Installation

Clone the repository:

```bash
git clone https://github.com/SanSanon/STUDENT-TASK-MANAGEMENT-USING-SQLITE.git
```

Navigate to the project directory:

```bash
cd Student-Management-System
```

Run the application:

```bash
python main.py
```

## Example Usage

```text
---- STUDENT MANAGEMENT SYSTEM ----
1. ADD Student
2. View Students
3. Delete Student
4. EXIT

Enter your choice: 1

Enter student id: 101
Enter student name: John
Enter student age: 20
Enter student grade: 85

Student added successfully!
```

### Viewing Students

```text
Enter your choice: 2

ID: 101, Name: John, Age: 20, Grade: 85
```

### Handling Duplicate Student IDs

```text
Enter your choice: 1

Enter student id: 101
Enter student name: Sarah
Enter student age: 21
Enter student grade: 90

Student ID already exists
```

### Deleting Students

```text
Enter your choice: 3

Enter student id: 101

Student Id 101 was deleted successfully
```

## Key Concepts Demonstrated

- **Layered Architecture:** Separating presentation, business logic, and database operations.
- **Separation of Concerns:** Assigning a specific responsibility to each application layer.
- **Object-Oriented Programming:** Using classes, constructors, methods, and instance attributes.
- **Dependency Injection:** Passing the repository object into the service class.
- **Database Management:** Performing CRUD-related SQL operations using SQLite.
- **Exception Handling:** Using `try`, `except`, and `raise` to manage invalid input and database constraints.
- **Data Persistence:** Preserving student records between application sessions.

## Future Improvements

- Update existing student information.
- Search for students by ID or name.
- Add email and other student attributes.
- Implement automated unit tests.
- Develop a graphical user interface (GUI).

## Author

**Wishtneiky Sanon**

Computer Science Student — Florida Atlantic University

## Project Purpose

Developed as part of a Python assignment focused on implementing Layered Architecture. The goal was to gain practical experience designing modular applications, managing databases, and applying object-oriented programming principles.
