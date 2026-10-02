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

    print("\n--- Student Details ---")

    for roll_no, details in students.items():
        print("Roll Number:", roll_no)
        print("Name:", details["name"])
        print("Course:", details["course"])
        print("----------------------")


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("\nStudent Found!")
        print("Roll Number:", roll_no)
        print("Name:", students[roll_no]["name"])
        print("Course:", students[roll_no]["course"])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    if roll_no in students:
        name = input("Enter New Name: ")
        course = input("Enter New Course: ")

        students[roll_no]["name"] = name
        students[roll_no]["course"] = course

        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


add_student()
display_students()
search_student()
update_student()
display_students()
delete_student()
display_students()