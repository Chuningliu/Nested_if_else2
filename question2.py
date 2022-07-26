# 2.Write a python program to find maximum between three numbers.


num=int(input("Enter the number"))
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
# if num>num1 or num>num2:
#     print(num,"is the maximum")
#     if num1>num or num1>num2:
#         print(num1,"is the maximum")
#     elif num2>num or num2>num1:
#         print(num2,"is the maximum")
#     # else:
#     #     print("Check it again")
# else:
#     print("One or both condition are equal")

if num>num1:
    if num>num2:
        print(num,"is max")
elif num1>num2:
    if num1>num:
        print(num1,"is max")
elif num2>num1 :
    if num2>num:
        print(num2,"is max")
else:
    print("one or both condition is equal")