#Decoratores

def my_decorator(func):
    def wrapper():
        print("before")
        print("call me")
        func()
        print("after")
        print("dont call me")
    return wrapper()
@my_decorator
def do_fast():
        print("slow")
