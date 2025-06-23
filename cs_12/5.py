def get_student_details():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    return "Name: " + name + ", Grade: " + grade + "\n"

def view_grades():
    try:
        f = open("grades.txt", "r")
        print("\nStudent Grades:")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("No grades file found !")

while True:
    print("1. Add student grades")
    print("2. View student grades")
    print("3. Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        f = open("grades.txt", "a")
        for i in range(1, 6):
            print("\nStudent", i)
            detail = get_student_details()
            f.write(detail)
        f.close()
        print("Student grades saved in grades.txt")
    elif ch == "2":
        view_grades()
    elif ch == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice , Try again !")