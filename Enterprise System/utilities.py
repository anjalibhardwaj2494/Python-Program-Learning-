# Importing Required Libraries
import pickle

def addcustomer():
    file=open("customer.bin","ab") #open the file
    cid=input("Enter the Customer ID: ")
    cname=input("Enter the Customer Name: ")
    cadd=input("Enter the Customer Address: ")
    cmob=input("Enter the Customer Mobile: ")
    cus=[cid,cname,cadd,cmob]
    pickle.dump(cus,file) # this is to add data into file
    file.close()
    print("Customer Added Successfully..")


def viewcustomer():
    file=open("customer.bin","rb")

    try:
        while True:
            data=pickle.load(file)
            print("Customer ID: ",data[0])
            print("Customer Name ",data[1])
            print("Customer Address: ",data[2])
            print("Customer Mobile: ",data[3])
            print("\n ---------------------------------")
    except:
        print("All Customer Loaded successfully !..")
    file.close()


def deletecustomer():
    file=open("customer.bin","rb")
    customer=[]
    flag=0
    cid=input("Enter the customer id you want to delete: ")
    try:
        while True:
            data=pickle.load(file) # we load file data to "data"
            if cid!=data[0]:
                customer.append(data) #we append all data to Customer list without required cid
            else:
                flag=1
    except:
        pass
    file.close()
    file=open("customer.bin","wb")
    for cus in customer:
        pickle.dump(cus,file)
    file.close()
    if flag==1:
        print("Customer Deleted Successfully!..")
    else:
        print("Customer Not Found!..")

def addproduct():
    file=open("product.bin","ab")
    pid=input("Enter the Product ID: ")
    pname=input("Enter the Product Name: ")
    price=input("Enter the Product Price: ")
    pdesc=input("Enter the Product Description: ")
    data={pid:[pname,price,pdesc]}
    pickle.dump(data,file)
    print(data)
    file.close()
    print("Product Added Successfully!.....")

def viewproduct():
    file=open("product.bin","rb")
    try:
        while True:
            product=pickle.load(file)
            

            for pid,data in product.items():
                print(" Product ID is: ",pid)
                print(" Product name is: ",data[0])
                print(" Product price is: ",data[1])
                print(" Product decription is: ",data[2])
                print("\n--------------------------------")
            
    except:
        print("Here's your all Product..")
    file.close()

def updateproprice():
    file=open("product.bin","ab")
    pid=input("Enter the Product Id you want to edit the price")
    list=[]
    flag=0
    try:
        while True:
            product=pickle.load(file)
            for pid,data in product.items():
                 if pid==product.key():
                     print("Product ID: ",pid)
                     print("Product name: ",data[0])
                     print("Product existing price",data[1])
                     print(" Product decription is: ",data[2])
                     price=input("Enter the new price")
                     list.append({pid:[data[0],price,data(2)])
                     


                
                     data[1]=np
                     flag=1
                 else:
                     print("Product Key is not available")
            
            for pid,data


        

