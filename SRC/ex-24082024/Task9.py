# factorial of 5

num=int(input("enter the number\n"))
fact=1
if num==0 or num==1:
    print(1)
else:
    for i in range(1,num+1,1):
        fact=fact*i
        print(fact)
