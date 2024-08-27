# multiple argument with no limit

def print_argument(*args):
    print(args[0])

print_argument("amit", "pramod", "ram")
print_argument("!@#","hello","o")
print_argument("a","b","c","d")

def multi(*args):
    for i in args:
        print(i)

multi("a", "b", "c")
multi("e", "b", "c")


