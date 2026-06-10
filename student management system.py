students = []

def add_student():

    # Student ID Validation
    while True:
        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            print("Please Enter student id.")
            continue

        if not student_id.isdigit():
            print("Student ID must contain numbers only.")
            continue

        student_id = int(student_id)
        break

    # Name Validation
    while True:
        name = input("Enter Name: ").strip()

        if name == "":
            print("Please Enter Name.")
        else:
            break

    # Course Validation
    while True:
        course = input("Enter Course: ").strip()

        if course == "":
            print("Please Enter Course.")
        else:
            break

    # Marks Validation
    while True:
        marks = input("Enter Marks: ").strip()

        if marks == "":
            print("Please Enter your Marks.")
            continue

        try:
            marks = float(marks)

            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.\nPlease Enter Valid Marks.")

        except ValueError:
            print("Please enter valid marks.")

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student Added Successfully!\n")


# View Students
def view_students():
    if len(students) == 0:
        print("No Student Records Found.\n")
        return

    print("\nStudent Records:\n")
    for student in students:
        print(f"ID     :{student['id']}")
        print(f"Name   :{student['name']}")
        print(f"Course :{student['course']}")
        print(f"Marks  :{student['marks']}")
        print("_"*40)
    print()


# Search Student
def search_student():
    student_id = int(input("Enter Student ID to Search: "))

    for student in students:
        if student["id"] == student_id:
            print("Student Found:")
            print(f"ID     :{student['id']}")
        print(f"Name   :{student['name']}")
        print(f"Course :{student['course']}")
        print(f"Marks  :{student['marks']}")
        print("_"*40)
        return

    print("Student Not Found.\n")


# Update Student
def update_student():
    student_id = int(input("Enter Student ID to Update: "))

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("Student Updated Successfully!\n")
            return

    print("Student Not Found.\n")


# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found.\n")


# Main Menu
while True:
    print("==================== Student Management System ====================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.\n")