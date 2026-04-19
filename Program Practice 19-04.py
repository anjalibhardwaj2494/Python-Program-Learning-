"""

#### Pattern Building

*****
*****
*****
*****
*****

for i in range (1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

*
**
***
****
*****
for i in range (1,6):
    for j in range(1,6):
        if(j<i+1):
           print("*",end=" ") 
        else:
            break
    print()


===================

for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" ") 
    print()

1
12
123
1234
12345

for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()

1
23
456
78910

a=1
for i in range (1,5):
    for j in range(1,i+1):
        print(a,end="")
        a=a+1
    print()


A
AB
ABC
ABCD
ABCDE

for i in range (1,6):
    for j in range(1,i+1):
        print(chr(j+64),end="") 
    print()

A
BB
CCC
DDDD
EEEEE

c=64
for i in range (1,6):
    for j in range(1,i+1):
        print(chr(c+i),end="") 
    print()

    ===========print(ord('A'))
A
BC
DEF
GHIJ
KLMNO
k=65

for i in range (1,6):
    for j in range(1,i+1):
        print(chr(k),end="")
        k=k+1
    print()
"""






    
