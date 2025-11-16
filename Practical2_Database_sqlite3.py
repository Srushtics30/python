import sqlite3
connection = sqlite3.connect("student.db")
print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("create table student(name varchar, rollno int, email varchar, contact int, course varchar)")

cursor.execute("insert into student values('A', 1, 'nkm@gmail.com, 873221, 'CS')")
cursor.execute("insert into student values('B', 2, 'nskd@gmail.com, 092321, 'IT')")
cursor.execute("insert into student values('C', 3, 'kald@gmail.com, 6553, 'CS')")
cursor.execute("insert into student values('D', 4, 'maso@gmail.com, 86422, 'CS')")

roll = 2
corse = "CS"
cursor.execute("update student set course = ? where rollno = ?"(,roll,corse))

rmv ="D"
cursor.execute("delete from student where name = ?",(rmv,))

rows = cursor.execute("select name, rollno, email, contact, course from student")

connection.commit()
print("Data inserted successfully")
print(rows)

connection.close()
