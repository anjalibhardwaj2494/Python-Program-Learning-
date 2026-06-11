#Exception Handling
"""
a= int(input("Enter A number: "))
b= int(input("Enter B number: "))
print("Division Started")
try:
    print("Division: ",a/b)
except:
    print("Found an Error!..")
print("Division Completed")

a= int(input("Enter A number: "))
b= int(input("Enter B number: "))
print("Division Started")
try:
    print("Division: ",a/b)
except ZeroDivisionError as e:
    print("Error:" ,e)
print("Division Completed")

print("Division Started")
try:
    a= int(input("Enter A number: "))
    b= int(input("Enter B number: "))
    print("Division: ",a/b)
    print(a[0])
except Exception as e:
    print("Error:" ,e)
print("Division Completed")
"""
age= int(input("Enter your age"))

try:
    assert age>18 , "Age should be 18+"
except AssertionError as e:
    print("Error: ",e)
else:
    print("Welcome!")

