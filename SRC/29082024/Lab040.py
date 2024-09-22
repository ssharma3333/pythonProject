list_of_unique_items={1,2,3,4,5,5,5}
print(list_of_unique_items)
List1=[12,23,34,45,56,56]
set1=set(List1)
print(set1)

t=( "for","amit","for")
print(t)
print(set(t))


set1={1,2,3,4,7,5,6}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)
my_set=set1.intersection(set2)
print(my_set)
my_set=set1.difference(set2)
print(my_set)
my_set=set2.difference(set1)
print(my_set)
subset=set2.issubset(set1)
print(subset)
set1.add("pramod")
print(set1)


