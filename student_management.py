students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    students[roll_no] = {
        "name": name,
        "course": course
    }

    print("Student added successfully!")

def display_students():
    if not students:
        print("No students found.")
        return

    for roll_no, details in students.items():
        print("\nRoll Number:", roll_no)
        print("Name:", details["name"])
        print("Course:", details["course"])

add_student()

print(students)
