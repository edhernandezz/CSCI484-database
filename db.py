# These are the datastructures and functions we need from the database
import psycopg2
import os

try:
    conn = psycopg2.connect(
        dbname=os.environ['DBNAME'],
        user=os.environ['DBUSER'],
        host=os.environ['DBHOST'],
        password=os.environ['DBPASSWORD'])
    curs=conn.cursor()
except:
    print("I am unable to connect to the database")

# pure database functionality for a student
def insertStudent(first,last,major,phone):
    query=f"""insert into students 
      (first,last,phone,major) 
      values ('{first}','{last}','{phone}','{major}');"""
    #print(query)
    curs.execute(query)
    conn.commit()

def deleteStudent():
    # Assignment for students to write this code.
    pass

def getStudent(id):
    query=f"""
      select first,last,phone,major,id from students where id={id};"""
    curs.execute(query)
    rows = curs.fetchall()
    return rows[0]

def getStudents():
    query=f"""
      select id,first,last,phone,major from students order by id;"""
    curs.execute(query)
    rows = curs.fetchall()
    return rows

def changeStudent(id,first,last,major,phone):
    values=""
    comma=False
    if len(first)>0:
        values+=f"first='{first}'"
        comma=True
    if len(last)>0:
        if (comma):
            values+=','
        values+=f"last='{last}'"
        comma=True
    if len(major)>0:
        if (comma):
            values+=','
        values+=f"major='{major}'"
        comma=True
    if len(phone)>0:
        if (comma):
            values+=','
        values+=f"phone='{phone}'"
        comma=True
    if (comma):
      query=f"""update students 
        set {values} 
        where id={id};"""
      curs.execute(query)
      conn.commit()

def getWidth(rows,tupleIndex,minimum):
    widths=[minimum]
    for r in rows:
        widths.append(len(str(r[tupleIndex])))
    return max(widths)

def getWidths(rows,mins):
    rowWidths=[]
    for i in range(0,5):
        rowWidths.append(getWidth(rows,i,mins[i]))
    return rowWidths

def outputHeader(w):
    return f"""|{"Id":{w[0]}}|{"First":{w[1]}}|{"Last":{w[2]}}|{"Phone":{w[3]}}|{"Major":{w[4]}}|\n"""

def headerWidths():
    return      [2,            5,               4,              5,               5]

def outputBreak(w):
    return f"""+{'':{'-'}<{w[0]}}+{'':{'-'}<{w[1]}}+{'':{'-'}<{w[2]}}+{'':{'-'}<{w[3]}}+{'':{'-'}<{w[4]}}+\n"""

def outputStudentRow(sInfo,w):
    return f"""|{sInfo[0]:{w[0]}}|{sInfo[1]:{w[1]}}|{sInfo[2]:{w[2]}}|{sInfo[3]:{w[3]}}|{sInfo[4]:{w[4]}}|\n"""

def showStudentsStr():
    students=getStudents()
    minWidths=headerWidths()
    widths=getWidths(students,minWidths)
    tableStr=outputBreak(widths)
    tableStr+=outputHeader(widths)
    tableStr+=outputBreak(widths)
    for student in students:
        tableStr+=outputStudentRow(student,widths)
    tableStr+=outputBreak(widths)
    return tableStr

if __name__=='__main__':
    addStudent("karl","castleton","CS","970-248-1837")
