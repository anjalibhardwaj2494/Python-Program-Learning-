"""

##Find the largest digit in a number.

num= int(input("Enter the number"))
a=1
while(num>0):
    b=num%10
    if(b>a):
        a=b
    num=num/10
print("Greatest Number is: ",int(a))

## WAP to print fibonaci series.

n=int(input( "enter the range of Fibonacci series"))
a=0
b=1
m=1
while (m<=n):
    c=a+b
    print(c, end=' ')
    m=m+1
    a=b
    b=c

"""





    
    
    
    
    
