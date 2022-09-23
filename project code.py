import mysql.connector as m
from tabulate import tabulate

def MainMenu():
    while True:
        print("\n")
        print("****WELCOME TO SCHOOL LIBRARY MANAGEMENT SYSTEM****\n")
        print("****CHOOSE TASK TO PERFORM****")
        print("1.To Perform Addtion,Display,Search,Deletion,Updation of Library Records")
        print("2.To Perform Addtion,Display,Search,Deletion,Updation of Student Records")
        print("3.To Display the Final Report Generated")
        print("4.To Exit the Program\n")
        N=int(input("Enter your choice:"))
        if N==1:
            print("****CHOOSE TASK TO PERFORM IN BOOKS RECORD****\n")
            print("1.Add Book Record")
            print("2.Show Book Details")
            print("3.Search Book Details")
            print("4.Delete Book Details")
            print("5.Update Book Details\n")
            a=int(input("Enter choice between 1-5"))
            if a==1:
                Add_Records()
            elif a==2:
                Show_Book_Records()
            elif a==3:
                Search_Book_Details()
            elif a==4:
                Delete_Book_Details()
            elif a==5:
                Update_Book_Details()
        elif N==2:
           print("****CHOOSE TASK TO PERFORM IN STUDENTS RECORD****\n")
           print("1.Add Student Record")
           print("2.Show Student Details")
           print("3.Search Student Records")
           print("4.Delete Student Records")
           print("5.Update Student Record\n")
           b=int(input("Enter a Number from 1-5"))
           if b==1:
               Add_Records1()
           elif b==2:
               Show_Stu_Records1()
           elif b==3:
               Search_Stu_Details1()
           elif b==4:
               Delete_Stu_Details1()
           elif b==5:
               Update_Stu_Details1()
        elif N==3:
           print("1.Report Generation of Book Records")
           print("2.Report Generation of Student Records\n") 
           c=int(input("Enter number 1 or 2"))
           if c==1:
               Rep_Gen_Lib()
           elif c==2:
               Rep_Gen_Stu()
        elif N==4:
            break
        else:
            print("Enter Number Between 1-4")
            
def Add_Records():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("connection established")
    CBook=input("Enter Book code")
    BName=input("Enter Book Name:")
    POB=float(input("Enter Price of the Book: Rs."))
    P_Book=input("Enter Publication of Book")
    Quant=int(input("Enter Quantity of Book"))
    query='''Insert into lib_Book
    values('%s','%s',%s,'%s',%s)'''%(CBook,BName,POB,P_Book,Quant)
    cur.execute(query)
    con.commit()
    print("Record has been saved in lib_Book table")

def Show_Book_Records():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    cur.execute("select * from lib_Book")
    data=cur.fetchall()
    print("****Displaying records****")
    print("\n"*2)
    for row in data:
        print(row)

def Search_Book_Details():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("****Displaying already existing records****")
    print("\n"*2)
    cur.execute("select * from lib_Book")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("\n"*2)
    A=input("enter code of Book you want to search")
    St=("select * from lib_Book where CBook='%s'"%(A))
    cur.execute(St)
    data=cur.fetchall()
    print("****Displaying records****")
    print("\n"*2)
    for row in data:
        print(row)

def Delete_Book_Details():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("****Displaying already existing records****")
    print("\n"*2)
    cur.execute("select * from lib_Book")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("\n"*2)
    A=input("Enter Code of Book you want to delete:")
    St=("Delete from lib_Book where CBook='%s'"%(A))
    cur.execute(St)
    con.commit()
    print("data deleted successfully")

def Update_Book_Details():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("****Displaying already existing records****")
    print("\n"*2)
    cur.execute("select * from lib_Book")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("\n"*2)
    CBook=input("Enter Code of Book whose record you want to update")
    print("Choose what you want to Update\n")
    print("1:edit Book Name")
    print("2:edit price of book ")
    print("3:edit publication of book")
    print("4:edit quantity of book\n")
    choice=int(input("enter your choice"))
    if choice==1:
       New_n=input("Enter New Book Name")
       query='''Update lib_Book set BName='%s'
       where CBook='%s' '''%(New_n,CBook)
       cur.execute(query)
       con.commit()
       print("Name updated")
    elif choice==2:
       New_POB=float(input("Enter New Price of Book")) 
       query='''Update lib_Book set POB=%s
       where CBook='%s' '''%(New_POB,CBook)
       cur.execute(query)
       con.commit()
       print("Price of Book updated")
    elif choice==3:
       New_p_book=input("Enter New Publication of book")
       query='''Update lib_Book set P_Book='%s'
       where CBook='%s' '''%(New_p_book,CBook)
       cur.execute(query)
       con.commit()
       print("Publication of book updated")
    elif choice==4:
       New_Quant=int(input("Enter New Quantity of book"))
       query='''Update lib_Book set Quant=%s
       where CBook='%s' '''%(New_Quant,CBook)
       cur.execute(query)
       con.commit()
       print("Quantity of book updated")
       
def Add_Records1():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("connection established")
    CBook=input("Enter Book code")
    Name=input("Enter your Name:")
    Admno=int(input("Enter your Admission Number:"))
    nBook=input("Enter name of Book issued:")
    print("Enter the dates in the format of YY/MM/DD")
    DOI=input("Enter Date of Issue:")
    DOR=input("Enter Date of Return:")
    POB=float(input("Enter Price of the Book: Rs."))
    query='''Insert into lib_student
    values('%s','%s',%s,'%s','%s','%s',%s)'''%(CBook,Name,Admno,nBook,DOI,DOR,POB)
    cur.execute(query)
    con.commit()
    print("Record has been saved in lib_student table")

def Show_Stu_Records1():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    cur.execute("select * from lib_student")
    data=cur.fetchall()
    print("****Displaying records****")
    print("\n"*2)
    for row in data:
        print(row)

def Search_Stu_Details1():
    print("\n"*3)
    con=m.connect(host="localhost",
                      user="root",
                      password="262816",
                      database="library")
    cur=con.cursor()
    print("****Displaying already existing records****")
    print("\n"*2)
    cur.execute("select * from lib_student")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("\n"*2)
    A=int(input("enter your admission number"))
    St=("select * from lib_student where Admno='%s'"%(A))
    cur.execute(St)
    data=cur.fetchall()
    print("****Displaying records****")
    print("\n"*2)
    for row in data:
        print(row)
        
def Delete_Stu_Details1():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("****Displaying already existing records****")
    print("\n"*2)
    cur.execute("select * from lib_student")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("\n"*2)
    A=input("Enter Admission number whose record you want to delete:")
    St=("Delete from lib_student where Admno='%s'"%(A))
    cur.execute(St)
    con.commit()
    print("data deleted successfully")

def Update_Stu_Details1():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    print("****Displaying already existing records****")
    print("\n"*2)
    cur.execute("select * from lib_student")
    data=cur.fetchall()
    for row in data:
        print(row)
    print("\n"*2)
    Admno=int(input("Enter Admission number whose record you want to update"))
    print("Choose what you want to Update\n")
    print("1:edit Name")
    print("2:edit date of issue")
    print("3:edit date of return")
    choice=int(input("enter your choice"))
    if choice==1:
       New_n=input("Enter New Name")
       query='''Update lib_student set Name='%s'
       where Admno=%s'''%(New_n,Admno)
       cur.execute(query)
       con.commit()
       print("Name updated")
    elif choice==2:
       New_DOI=input("Enter New Date of Issue")
       query='''Update lib_student set DOI='%s'
       where Admno=%s'''%(New_DOI,Admno)
       cur.execute(query)
       con.commit()
       print("Date of Issue of book updated")
    elif choice==3:
       New_DOR=input("Enter New Date of Return")
       query='''Update lib_student set DOR='%s'
       where Admno=%s'''%(New_DOR,Admno)
       cur.execute(query)
       con.commit()
       print("Date of return of book updated")
    
def Rep_Gen_Lib():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    cur.execute("select * from lib_Book")
    result=cur.fetchall()
    print("****Displaying Final Books Report Generated\n") 
    print(tabulate(result,headers=['Book Code','Book Name','Price of Book',
                                   'Publisher','Quantity'],tablefmt='psql'))
               
def Rep_Gen_Stu():
    print("\n"*3)
    con=m.connect(host="localhost",
                  user="root",
                  password="262816",
                  database="library")
    cur=con.cursor()
    cur.execute("select * from lib_student")
    result=cur.fetchall()
    print("****Displaying Final Students Report Generated\n")
    print(tabulate(result,headers=['Book Code','Student Name','Admission No.',
                                   'Book Name','Date of Issue','Date of Return',
                                   'Price of Book'],tablefmt='psql'))
               

MainMenu()



