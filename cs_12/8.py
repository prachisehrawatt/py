'''1. Student Marks Manager
Create a CSV file named `students.csv` with the following columns:
`roll_no`, `name`, `math`, `science`, `english`
Now, write a Python program to:
- Read the CSV file.
- Calculate the total and average marks for each student.
- Print the result as a formatted table.'''

import csv
f=open('extension.csv','r')
obj= csv.reader(f)
students = []

for row in obj:
        math = row['math']
        science = row['science']
        english = row['english']

        total = math+science+english
        average = round(total / 3)

        row['total'] = total
        row['average'] = average

        students.append(row)


