class Student:
    def __init__(self, usn, name, marks):
        self.usn = usn
        self.name = name
        self.marks = marks

    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("------------------------") 

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        usn = input("Enter USN: ")
        for student in self.students:
            if student.usn == usn:
                print("Student with this USN already exists.")
                return  # Fixed: return is now inside the if block
        
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = Student(usn, name, marks)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
            return  # Fixed: return is now inside the if block
        
        for student in self.students:
            student.display()

    # Searching student by USN
    def search_student(self):
        usn = input("Enter USN to search: ")
        for student in self.students:
            if student.usn == usn:
                print("Student found:")
                student.display()
                return  # Fixed: return is now inside the if block
        print("Student not found.")

    # Deletion of student       
    def delete_student(self):
        usn = input("Enter USN to delete: ")
        for student in self.students:
            if student.usn == usn:
                self.students.remove(student)
                print("Student deleted successfully!")
                return  # Fixed: return is now inside the if block
        print("Student not found.")

app = StudentManagement()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        app.add_student()
    elif choice == '2':
        app.view_students()
    elif choice == '3':
        app.search_student()
    elif choice == '4':
        app.delete_student()
    elif choice == '5':
        print("Thanking you for using the Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")