def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
choice = int(input("Enter your choice- \n 1.Addition\n 2.Substractions\n 3.Multiplication \n 4.Division \n"))
#what do I have: 2 numbers (a,b) and 1 choice
if choice == 1:
    print("addition of the numbers is : ",Addition(a,b))
elif choice == 2:
    print("subtraction of the numbers is : ",Subtraction(a,b))
elif choice == 3:
    print("multiplication of the numbers is : ",Multiplication(a,b))
elif choice == 4:
    print("division of the numbers is : ",Division(a,b))
else:
    print("default choice")