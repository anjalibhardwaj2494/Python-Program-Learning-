"""
STUDENT MANAGEMENT SYSTEM
Student (sid,sname,sadd,scourse)

1.Add Student
2.View all student
3.Delete Student
4.Update Student Info
0.Exit
"""
#Importing Module/Libraries

import utilis


#Data Storage
student= dict()
#print(type(student))

#Dashboard
while True:
    print("\n\t\t STUDENT MANAGEMENT SYSTEM")
    print('''
            1.Add Student
            2.View all student
            3.Delete Student
            4.Update Student Info
            0.Exit
    ''')
    ch=int(input("\n\tEnter your choice: "))
    if(ch==0):
        print("\n\tBye Bye Admin! ")
        break
    elif ch==1:
        student=utilis.addstudent(student)
        print(student)
        print("\n\tStudent Addes Sucessfully")
        input("\n\tPress Enter to continue..")
    elif ch==2:
        utilis.viewallstudent(student)
        print("\n\t Here is your all student: ")
        input("\n\tPress Enter to continue..")
    elif ch==3:
        student=utilis.deletestudent(student)
        input("\t\tPress Enter To Continue...")
    elif ch==4:
        student=utilis.updatestudent(student)
        input("\t\tPress Enter To Continue...")
    else:
        print("Wrong Entry")


    

    