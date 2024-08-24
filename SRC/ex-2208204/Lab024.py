i=0
while i<10:
    print(i)
    i=i+1

i=0
while i<5:
    print(i, end=" ")
    i=i+1

for i in range(2,22):
    print(i)
    if i==20:
        break

for i in range(0,10):
    if i==5 or i==6:
        print(i)
    else:
        pass

for i in range(2,30,4):
    if i%2==0:
        print(i)
    else:
        pass