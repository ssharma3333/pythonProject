
for number in range(10):
    if number%2==0:
        print(number)
    else:
        pass


for number in range(10):
    if number%2==0:
        continue
    else:
        print(number)

    for number in range(10):
        if number % 2 == 0:
            pass
        else:
            print(number)

for number in range(10):
    if number%2==0:
        print(number)
    else:
        continue