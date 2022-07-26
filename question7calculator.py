# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# Choice=input("Enter your choice:")
# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number 2:"))
# if Choice=="1":
#     print(num1,"+",num2,"=",(num1+num2))
# elif Choice=="2":
#     print(num1,"-",num2,"=",(num1-num2))
# elif Choice=="3":
#     print(num1,"*",num2,"=",(num1*num2))
# elif Choice=="4":
#     if num2==0.0:
#         print("Divide by 0, error")
#     else:
#         print(num1,"/",num2,"=",(num1/num2))
# else:
#     print("Invalid choice")



import  tkinter
from tkinter import *
root = tkinter.Tk()
root.geometry("300x300")
root.title("Try code")

entry = tkinter.Entry(root)
entry.pack()

def on_button():
    if entry.get() == "Screen""screen":
        slabel = tkinter.Label(root, text="Screen was entered")
        slabel.pack()
    else:
        tlabel = tkinter.Label(root, text="")
        tlabel.pack()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
Choice=input("Enter your choice:")
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if Choice=="1":
    print(num1,"+",num2,"=",(num1+num2))
elif Choice=="2":
    print(num1,"-",num2,"=",(num1-num2))
elif Choice=="3":
    print(num1,"*",num2,"=",(num1*num2))
elif Choice=="4":
    if num2==0.0:
        print("Divide by 0, error")
    else:
        print(num1,"/",num2,"=",(num1/num2))
else:
    print("Invalid choice")

