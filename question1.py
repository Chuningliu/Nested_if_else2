# 1.Write a python program to find maximum between two numbers.


# num=int(input("Enter the number1"))
# num1=int(input("Enter the number"))
# if num>num1:
#     print(num,"is greater than",num1)
# else:
#     print(num1,"is greater than",num)





Language=input("Enter the language")
Bank=input("Enter Bank name")
print("Welcome to",Bank)
Amount=20000
print("Insert your card")
print("Please wait.....")
pin=int(input("Enter the pin"))
if (pin==1234):
    print("1.Withdraw:")
    print("2.Balance enquiry:")
    print("3.Fast cash:")
    choice=int(input("Enter the transaction"))
    if choice==1:
        Withdraw=int(input("Enter the amount"))
        if Withdraw<Amount:
            print("Please take your amount", Withdraw)
        else:
            print("Invalid")
    elif choice==2:
        print("The available balance is",Amount)
    if choice==3:
        print("1->500")
        print("2->1000")
        print("3->2000")
        print("4->10000")
        option=int(input("Enter the fast cash"))
        if (option==1 and 500<Amount):
            print("Please take your cash 500") 
        elif option==2 and 1000<Amount:
            print("Please take your cash of 1000")
        elif option==3 and 2000<Amount:
            print("Please take your cash of 2000")
        elif option==4 and 10000<Amount:
            print("Please take your cash of 10000")
        else:
            print("Invalid fast cash")
    # else:
    #     print("Enter correct choice")
else:
    print("Enter the correct pin")
