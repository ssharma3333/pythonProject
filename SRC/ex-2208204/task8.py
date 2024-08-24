a=float(input("enter the value-"))
b=float(input("enter the value-"))
c=float(input("enter the value-"))

if a==b==c:
    print("equilateral")
elif a==b or b==c or a==c:
    print("sosceles")
else:
    print("scalene")