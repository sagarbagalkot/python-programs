#python program to demostrate database using sqlite3
print("U15IG22S0054")
import sqlite3 as sql
con=sql.connect("example.db")
cur=con.cursor()
sql="""
create table if not exists student
(
rno varchar(10),
name varchar(10),
primary key(rno)
)
"""
cur.execute(sql)
cur.execute("delete from student")
con.commit()
print("Table created")
for i in range(1,6):
    rno=input(f"enter rollno of {i} student")
    name=input(f"enter name {i} student")
    cur.execute("insert into student(rno,name) values(?,?)",(rno,name))
con.commit()
print("data inserted")
def display():
    global cur
    cur.execute("select * from student")
    rows=cur.fetchall()
    print("student data are as follows")
    print("rollono|\tname\t|")
    for row in rows:
        rno=row[0]
        name=row[1]
        print(f"{rno}|\t{name}\t|")
display()
rno=input("enter the rollono you want update")
name=input("enter correct name")
cur.execute("update student set name=? where rno=?",(name,rno))
con.commit()
print("data deleted")
display()
rno=input("enter the rollono you want delete")
cur.execute("delete from student where rno=?",(rno,))
con.commit()
print("data deleted")
display()
con.close()