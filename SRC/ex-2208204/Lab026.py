browser_name=input("enter the name of the browser-")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        print("excute the firefox code")
    case "chrome":
        print("excute the chrome code")
    case "edge":
        print("excute the edge code")
    case _:
        print(" Browser not found")


user_type=input('enter the name admin, manger\n')
user_type=user_type.lower()
match user_type:
    case "admin":
        print("hi sir")
    case "manger":
        print("hello sir")
    case _:
        print(" good bye")

