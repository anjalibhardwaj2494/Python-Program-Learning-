"""

for i in range (1,10,1):
    print("Hello World")
    
===============

print(range(1,10,2))
print(*range(1,20,2))

==================
print("Hello",end=" ")
print("India")
==========================
## WAP to program to write a program from 1 to 10.

for i in range(1,11,1):
    print(i)

=========================

## WAP to program to write a program from 10 to 1.
for i in range(10,0,-1):
    print(i)
======================
## WAP to program to write a program from 1 to n.

n= int(input(" Enter the value of n"))
for i in range (1,n+1,1):
       print(i)

========================


##WAP to find all the facors of a number

n= int(input ("Enter a number: "))
for i in range(1,n+1,1):
    if(n%i==0):
        print(i)
else:
    print(" Number is zero")
    
========================

##WAP to find  the count of facors of a number

n= int(input("Enter a number"))
count=0
print("Factors are")
for i in range(1,n+1):
    
    if(n%i==0):
        count=count+1
        print(i)
print("Total number of factor is " ,count)

======================

## WAP to check If the number is prime or not

n= int(input("Enter the number"))
count=0
for i in range (1,n+1):
    if(n%i==0):
        count=count+1
if count==2:
    print("Number is prime")
else:
    print("Number is not prime")


====================

## Break

for i in range(1,10):
    if(i==4):
        break
    print(i)
======================
for i in range(1,10):
    print(i)
    if(i==4):
        break

=========================

for i in range(1,10,2):
    if(i==4):
        break
    print(i)

=============================
## WAP to find all prime number from 1 to 50.



for n in range (1,51):
    count=0
    for i in range(1,n+1):
        if (n%i==0):
            count=count+1
    if (count==2):
        print(n)


####While Loop

a=1
while(a<5):
    print("Hello")
    a=a+1
"""

ch='y'
while ch in "Yy":
    sid= input("Enter studentID")
    sname= input("Enter student name")
    ch=input("Enter your choice Y/N : ")
    

    
          




        
       



