def say_hello_default(name="pramod"):
    print("hello",name.lower())
say_hello_default("name")
say_hello_default("swati")
say_hello_default("vishal")


def multiple_people_name(name1="pramod",name2="amit",name3="ram"):
    print("my name is-,",name1,name2,name3)
multiple_people_name()

multiple_people_name(name1="shayam",name2="a",name3="B")

def number(num1=5,num2=10):
    print("number",num1,num2)

number(num1=4,num2=45)

def number(num1=5,num2=10):
    return num1+num2
result=number()
print(result)


def number(num1=5,num2=10):
    return num1+num2
result=number(6,7)
print(result)

def number(num1=5,num2=10):
    return num1+num2
result=number(num1=10,num2=20)
print(result)

def number(num1,num2):
    return num1+num2
result=number(2,3)
print(result)
