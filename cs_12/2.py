def get_student_details():
    return 

f = open('marks.txt', 'w')
while True:
    print('Press 1 : Enter details of student.')
    print('Press 2 : Exit')
    ch = input('Enter your choice : ')
    if ch == '1':
        f.write(get_student_details())
    elif ch == '2':
        break
    else :
        print('entered wrong input !')