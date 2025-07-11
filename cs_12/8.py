import csv
f=open("stu.csv","r")
obj=csv.reader(f, delimiter='\t')
stu_count = 0
for i in obj:
    if stu_count == 0:
        print(",".join(i) , "average marks")
        stu_count = stu_count + 1
    else:
        avg_marks = (int(i[2]) + int(i[3]) + int(i[4])) / 3
        print(' '.join(i),' \t ',int(avg_marks))