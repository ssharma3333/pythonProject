my_tuple=("Amit","alok")
print(my_tuple)
my_api_list=list(my_tuple)
print(my_api_list)
my_api_list.append(4)
print(my_api_list)
my_tuple1=tuple(my_api_list)
print(my_tuple1)

hero1=("batsman","wonder women")
hero2=("dina","hero")
hero3=(hero1,hero2)
print(hero3)

print(hero3[0])
print(hero3[0][1])
print(hero3[1][1])


cities=("amit","pramod")
print("amit" in cities)
print("vishal"in cities)
