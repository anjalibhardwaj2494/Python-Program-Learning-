"""
class my_class:
    x=10
    def abc(a):
        print("Hello India")

obj=my_class()
print(obj.x)
obj.abc()

obj1= my_class()
obj2=my_class()
obj3=my_class()
obj2.x=100
print(obj3.x)
print(obj2.x)


class utility:
    x=100
    def abcd(self):
        print("I am myfunc from class utility")
obj=utility()
print(obj.x)
obj.abcd()


class utility:
    x=100
    def abcd(self):
        print("Value of x is: ",self.x)
obj=utility()
print(obj.x)
obj.abcd()

class A:
    def add(self,a,b):
        return a+b

class B(A):
    def add(self):
        print("Hello World")

obj=B()
obj1=A()
obj.add()
print(obj1.add(10,20))
"""
#Abstraction

from abc import ABC,abstractmethod
class services(ABC):
    @abstractmethod
    def prereq(self):
        pass
    def serv1(self):
        print("I am service 1. ")
    def serv2(self):
        print("I am service 2.")

class myclass(services):
    def prereq(self):
        pass
    def myfun(self):
        print("I am myfunc from Myclass. ")


obj=myclass()
obj.myfun()
obj.serv1()

