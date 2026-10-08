# This is the code for the Text UI interface to the students table

def addStudent():
    print("Enter the following information for the new student")
    first=input("First Name: ")
    last=input("Last Name: ")
    major=input("Major: ")
    phone=input("Phone: ")
    insertStudent(first,last,major,phone)

def outputStudent(studentInfo):
    print(f"Id:{studentInfo[4]}")
    print(f"First: {studentInfo[0]} Last:{studentInfo[1]}")
    print(f"Phone: {studentInfo[2]} Major: {studentInfo[3]}")

def showStudent():
    print("Enter the id information for the student")
    id=input("Id: ")
    studentInfo=getStudent(id)
    #print(rows)
    outputStudent(studentInfo)

def showStudents():
    studentsOutput=showStudentsStr()
    print(studentsOutput)

def updateStudent():
    print("Enter the following new information for the existing student")
    id=input("Id: ")
    first=input("First Name: ")
    last=input("Last Name: ")
    major=input("Major: ")
    phone=input("Phone: ")
    changeStudent(id,first,last,major,phone)

if __name__=='__main__':
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

