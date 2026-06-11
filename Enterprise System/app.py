# EnterPrise Inventory System

from utilities import addcustomer,viewcustomer,deletecustomer,addproduct,viewproduct


while True:
    print("""
    ### Harsh Enterprises ###
            
    1. Add a Customer
    2. View all Customer
    3. Delete a Cutomer
    4. Add a Product
    5. View a Product
    6. Update the Product Price
    7. Place an Order
    8. View all Orders
    9. View Orders by Customer
    0. Exit
            """ )

    ch= int(input("Enter your Choice: "))

    if ch==0:
        print("Bye Bye Admin !")
        break

    elif ch==1:
        addcustomer()
        input("Press Enter to continue...")

    elif ch==2:
        viewcustomer()
        input("Press Enter to continue...")

    elif ch==3:
        deletecustomer()
        input("Press Enter to continue...")

    elif ch==4:
        addproduct()
        input("Press Enter to continue...")

    elif ch==5:
        viewproduct()
        input("Press Enter to continue...")


else:
    print("You ENtered worng choice!")