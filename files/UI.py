# import psycopg2

# try:
#     conn = psycopg2.connect(
#         dbname='mydata2',
#         user='karl3',
#         host='localhost',
#         password='password')
#     curs=conn.cursor()
# except:
#     print("I am unable to connect to the database")


def addStudent():
    print("Enter the following information for the new student")
    first=input("First Name: ")
    last=input("Last Name: ")
    major=input("Major: ")
    phone=input("Phone: ")
    query=f"""insert into students 
      (first,last,phone,major) 
      values ('{first}','{last}','{phone}','{major}');"""
    #print(query)
    curs.execute(query)
    conn.commit()

def deleteStudent():
    # Assignment for students to write this code.
    pass

def showStudent():
    print("Enter the id information for the student")
    id=input("Id: ")
    query=f"""
      select first,last,phone,major from students where id={id};"""
    curs.execute(query)
    rows = curs.fetchall()
    #print(rows)
    print(f"First: {rows[0][0]} Last:{rows[0][1]}")
    print(f"Phone: {rows[0][2]} Major: {rows[0][3]}")

def showStudents():
    query=f"""
      select id,first,last,phone from students order by id;"""
    curs.execute(query)
    rows = curs.fetchall()
    #print(rows)
    for row in rows:
        print(f"Id: {row[0]}")
        print(f"First: {row[1]} Last:{row[2]}")
        print(f"Phone: {row[3]}")

def updateStudent():
    print("Enter the following new information for the existing student")
    id=input("Id: ")
    first=input("First Name: ")
    last=input("Last Name: ")
    major=input("Major: ")
    phone=input("Phone: ")
    query=f"""update students 
      set first='{first}',last='{last}',phone='{phone}',major='{major}' 
      where id={id};"""
    curs.execute(query)
    conn.commit()  

choice="1"
while (choice!='0'):
    print("!!!!!!MENU!!!!!!")
    print("1) Add a student")
    print("2) Delete a student")
    print("3) Show a student")
    print("4) Update a student")
    print("5) Show all Students")
    print("0) Quit")
    choice=input("Type the number for your choice: ")
    if (choice=='1'): 
        addStudent()
    if (choice=='2'):
        deleteStudent()
    if (choice=='3'):
        showStudent()
    if (choice=='4'):
        updateStudent()
    if (choice=='5'):
        showStudents()

