# function - which reusable
def greet():
    print("hello there!!")
greet()

def greet_to_all_of_you():
    print("Hello, Everyone")
greet_to_all_of_you()

def greet_to_all_of_you(name):
    print(name)
greet_to_all_of_you("swati")

def greet_to_all_of_you(name):
    print("hello,", name.upper())

greet_to_all_of_you("pramod")
greet_to_all_of_you("AMit")
greet_to_all_of_you("123")
greet_to_all_of_you("3.14")

def greet(name):
    print("hello,", name.lower())
name=input("enter you name\n")
greet(name)