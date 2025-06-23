def get_student_details():
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = input("Marks: ")
    return roll + "," + name + "," + marks + "\n"

while True:
    print("1. Add student\n2. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        f = open("marks.txt", "w")
        n = int(input("How many students? "))
        for i in range(n):
            print("Student" , i+1)
            f.write(get_student_details())
        f.close()
        print("saved in marks.txt")
    elif ch == "2":
        break
    else:
        print("Wrong choice")