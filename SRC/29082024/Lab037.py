my_list1=[1,2,3]
my_list2=["pramod",55]
print(my_list1)
print(my_list2)
print(len(my_list1))
print(len(my_list2))
print(my_list1[0])
print(my_list2[1])
print("element at index 0", my_list1[0])
for element in my_list1:
     print(element)
my_list1.append(4)
print(my_list1)

my_list1.extend([4,5,6])
print(my_list1)

my_list1.insert(1,"amit")
print(my_list1)

my_list2.clear()
print(my_list2)


my_list2.insert(-1,"lucky")
print(my_list2)

my_list2.remove("pramod")
print(my_list2)

my_list3=my_list1.copy()
print(my_list3)
print(my_list1)