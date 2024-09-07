def outer_function():
    var=30
    def inner_function1():
        print(var)

    def inner_function2():
        print(var)
    inner_function1()
    inner_function1()

outer_function()


