"""
##If

if(50>10):
    print("Hello World")

    =============================
 ## If_else

a= int(input("Enter the value od a: " ))
if(a>10):
    print("Hello")
else:
    print("Bye")


=============================

if (10>5):
    print("Hello")
print("Bye")

======================================
if (10>50):
    print("Hello")
print("Bye")
============================

# WAP to find greater between two numbers.

a= int(input("Enter the value of a: " ))
b= int(input("Enter the value of b: " ))
if(a>b):
    print("a is greater than b.")
else:
    print("b is greater than a")

======================================

# WAP to check entered number is even or odd.

a= int(input("Enter a number: " ))
if(a%2==0):
    print(" Number is even ")
else:
    print("Number is odd")
========================================


#### Nested IF :

#WAP to find greater between two numbers also check for equal.

a= int(input("Enter the value of a: " ))
b= int(input("Enter the value of b: " ))
if(a==b):
    print("a is equal to b")
else:
    if(a>b):
        print("a is greater than b")
    else:
        print("b is greater than a")

==================================

###WAP to check if a numner is positive negative or zero.
    
a= int(input("Enter the value of a: " ))
if(a==0):
     print("Number is zero: ",a)
else:
    if(a>0):
        print(" NUmber is positive: ",a)
    else:
        print("Number is negative: " ,a)

===================================

## WAP to check if the entered character is vowel or constant.

ch= str(input("Enter a character: " ))
if(ch=='a'):
    print("character is vowel")
else:
    if(ch=='e'):
        print("character is vowel")
    else:
        if(ch=='i'):
            print("character is vowel")
        else:
            if(ch=='o'):
                print("character is vowel")
            else:
                if(ch=='u'):
                    print("character is vowel")
                else:
                    print("Character is consonant")

===================================================

## WAP to check if the entered character is vowel or constantusing elif

ch= str(input("Enter a character: " ))
if(ch=='a'):
    print("character is vowel")
elif(ch=='e'):
    print("character is vowel")
elif(ch=='i'):
    print("character is vowel")
elif(ch=='o'):
    print("character is vowel")
elif(ch=='u'):
    print("character is vowel")
else:
    print("Character is consonant")

===============================

## using complex condition:

ch= str(input("Enter a character: " ))
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("character is vowel")
else:
    print("Character is consonant")
"""

ch= str(input("Enter a character: " ))
if ch in "AEIOUaeiou":
    print("character is vowel")
else:
    print("Character is consonant")




    
    







    

