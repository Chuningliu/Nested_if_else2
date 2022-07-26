# # #  ATM QUESTION:

# Language=input("Enter the language, English or Hindi:")
# if Language=="English":
#     # print("Language not available")
#     Bank=input("Enter Bank name")
#     print("Welcome to",Bank)
#     Amount=20000
#     print("Insert your card")
#     print("Please wait.....")
#     pin=int(input("Enter the pin"))
#     if (pin==1234):
#        print("1.Withdraw:")
#        print("2.Balance enquiry:")
#        print("3.Fast cash:")
#        print("4.Transfer")
#        print("5.Deposit")
#        print("6.Exit")
#        choice=int(input("Enter the transaction:"))
#        if choice==1:
#          Withdraw=int(input("Enter the amount :"))
#          if Withdraw<Amount:
#             print("Please take your amount", Withdraw)
#             print("And the remaining balance is",Amount-Withdraw)
#          else:
#             print("Invalid")
#        elif choice==2:
#          print("The available balance is",Amount)
#        elif choice==3:
#         print("1->500")
#         print("2->1000")
#         print("3->2000")
#         print("4->10000")
#         option=int(input("Enter the fast cash :"))
#         if (option==1 and 500<Amount):
#             print("Please take your cash 500") 
#             print("The available balance is",Amount-500)
#         elif option==2 and 1000<Amount:
#             print("Please take your cash of 1000")
#             print("The available balance is",Amount-1000)
#         elif option==3 and 2000<Amount:
#             print("Please take your cash of 2000")
#             print("The available balance is",2000)
#         elif option==4 and 10000<Amount:
#             print("Please take your cash of 10000")
#             print("The available balance is",Amount-10000)
#         else:
#             print("Invalid fast cash")
#        elif choice==4:
#         Transfer=int(input("Enter the amount"))
#         if Transfer<=Amount:
#             print("Transfer successful")
#             print("Available balance is",Amount-Transfer)
#         else:
#             print("Transfer failed")
#        elif choice==5:
#         Deposit=int(input("Enter the amount"))
#         total=Amount+Deposit
#         print("Deposited amount is",Deposit)
#         print("And the remaining balance is",total)
#        elif choice==6:
#         print("Thank you for Banking with us")

#     else:
#         print("Enter correct pin")
# elif Language=="Hindi":
#     print("Language not available")
# else:
#     print("Enter the correct language")
