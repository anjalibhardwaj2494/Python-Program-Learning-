"""
file=open('Student.txt','a')
file.write(" Noida")
file.close()

li=["Aman Kumar\n","Sahil Kumar\n","Ashutosh Kumar"]
file=open('Student.txt','w')
file.writelines(li)
file.close()

file= open('Student.txt','r')
data=file.read()
print(data)
file.close()

file= open('Student.txt','r')
data=file.read(20)
print(data)
file.close()

file= open('Student.txt','r')
data=file.readline()
print(data)
file.close()

file= open('Student.txt','r')
data=file.readline()
print(data)
data=file.readline()
print(data)
file.close()




li=["Aman Kumar\n","Sahil Kumar\n","Ashutosh Kumar"]
file=open('Student.txt','w')
file.writelines(li)
file.close()


file= open('Student.txt','r')
for i in range (3):
    data=file.readline()
    print(data)
file.close()

file= open('Student.txt','r')
while True:
    data=file.readline()
    print(data)
    if len(data)==0:
        break
file.close()

file= open('Student.txt','r')
for i in range (3):
    data=file.readlines()
    print(data)
file.close()

file= open('Student.txt','r')
for i in range (3):
    data=file.readlines()
    for line in data:
        print(line)
    
file.close()

file=open('Student.txt','r')
#print(file.tell())
data=file.read(10)
print(data)
#file.seek(20)
print(file.read())
print(file.tell())
file.close()


import pickle
file =open('emp.bin','wb')
pickle.dump('Rahul Kumar',file)
file.close()
"""
import pickle
file= open('emp.bin','rb')
data=pickle.load(file)
print(data)
data=pickle.load(file)
print(data)
file.close()


