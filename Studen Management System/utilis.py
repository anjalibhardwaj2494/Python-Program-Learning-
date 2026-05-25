def addstudent(student):
    sid=input("Enter the student ID: ")
    sname=input("Enter the student Name: ")
    saddress=input("Enter the student Address: ")
    scourse=input("Enter the student Course: ")
    student.update({sid: [sname,saddress,scourse]})
    return student

def viewallstudent(student):
    for sid,data in student.items():
        print("\t\t Student ID: ",sid)
        print("\t\t Student Name: ",data[0])
        print("\t\t Student Address: ",data[1])
        print("\t\t Student Course: ",data[2])
        print("\t\t----------------------------")

def deletestudent(student):
    sid= input("Enter the student ID you want to delete")
    data=student.get(sid,"Student not found")
    if type(data)== list:
        print("Student Name",data[0])
        student.pop(sid)
        print("Student deleted sucessfully")
    else:
        print(data)
    return student

def updatestudent(student):
    sid= input("Enter the student id you want to update")
    data=student.get(sid,"Student not Found")
    if type(data)==list:
        print("Name of student: ",data[0])
        print("Student old address: ",data[1])
        add=input("Enter new address: ")
        print("Student old course: ",data[2])
        course=input("Enter new course : ")
        student.update({sid:[data[0],add,course]})
        print("Student Updated sucessfully...")
    else:
        print(data)
    return student






