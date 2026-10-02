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


add_student()

print(students)
