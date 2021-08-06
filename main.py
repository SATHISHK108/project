import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="",database="Students_data_management")
mycursor = mydb.cursor()


menu = {'1': 'add_student', '2': 'edit_student', '3': 'delete_student', '4': 'get all student', '5': 'get a student',
        '6': 'exit'}
for x, y in menu.items():
    print(x, y)

print("select the option")

a = int(input())

if a == 1:
        print("Entre student name")
        name = input()
        print("Entre Dept name")
        dept = input()
        print("Mark")
        s1 = int(input())
        s2 = int(input())
        s3 = int(input())
        s4 = int(input())
        s5 = int(input())
        total_mark = (s1 + s2 + s3 + s4 + s5)
        average = total_mark / 5

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        elif average >= 50:
            grade = 'E'
        else:
            grade = 'F'
        insert_data = (
        "INSERT INTO students_detail(Name,Department,S1,S2,S3,S4,S5,Total,Average,Grade)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (name,dept, s1, s2, s3, s4, s5, total_mark, average, grade)
        mycursor.execute(insert_data, data)
        print("student details add successfully")
        mydb.commit()


elif a == 2:
    mycursor.execute("SELECT Id,Name,Department FROM students_detail")
    for result in mycursor.fetchall():
     print(result)
    print("entre the Id of student")
    changes = int(input())
    search = f"""SELECT Name FROM students_detail WHERE Id = {changes}"""
    mycursor.execute(search)
    records = mycursor.fetchall()
    print(records)
    print("Entre student name")
    name = input()
    print("Entre Dept name")
    dept = input()
    print("Mark")
    s1 = int(input())
    s2 = int(input())
    s3 = int(input())
    s4 = int(input())
    s5 = int(input())
    total_mark = (s1 + s2 + s3 + s4 + s5)
    average = total_mark / 5

    if average >= 90:
         grade = "A"
    elif average >= 80:
         grade = "B"
    elif average >= 70:
         grade = "C"
    elif average >= 60:
         grade = "D"
    elif average >= 50:
         grade = "E"
    else:
         grade = "F"
    update = f"""UPDATE `students_detail` SET Name="{name}",Department="{dept}",S1="{s1}",S2="{s2}",S3="{s3}",S4="{s4}",S5="{s5}",Total="{total_mark}",Average="{average}",Grade="{grade}" WHERE Id = {changes}"""
    mycursor.execute(update)
    mydb.commit()


elif a == 3:
    mycursor.execute("SELECT Id,Name,Department FROM students_detail")
    for result in mycursor.fetchall():
        print(result)
    print("Enter the student Id")
    changes = int(input())
    search = f"""DELETE FROM students_detail WHERE Id = {changes}"""
    mycursor.execute(search)
    mydb.commit()

elif a == 4:
    mycursor.execute("SELECT * FROM students_detail")
    for result in mycursor.fetchall():
        print(result)

elif a == 5:
    mycursor.execute("SELECT Id,Name,Department FROM students_detail")
    for result in mycursor.fetchall():
        print(result)
    print("Enter student Id")
    a_student = int(input())
    student = f"""SELECT * FROM students_detail WHERE Id = {a_student}"""
    mycursor.execute(student)
    details = mycursor.fetchall()
    print(details)

elif a == 6:
    exit()



