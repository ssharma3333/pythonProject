num1=float(input("enter the num1\n"))
num2=float(input("enter the num2\n"))
num3=float(input("enter the num3\n"))
if num1>num2 and num1>num3:
    print("num1 is max",{num1})
elif num2>num1 and num2>num3:
    print("num2 is max",{num2})
else:
    print("num3 is max",{num3})