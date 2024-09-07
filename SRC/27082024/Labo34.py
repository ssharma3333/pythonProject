my_shopping_list=["milk","bread","butter"]



def bring_more_food(my_shopping_list):
    more_item=input("enter item\n")
    my_shopping_list.append(more_item)
    my_shopping_list.remove(more_item)
    my_shopping_list.insert(0,more_item)
    return my_shopping_list

l=bring_more_food(my_shopping_list)
print(l)

def add_more_list(my_list):
    my_list.append("cheese")
    my_list.remove("milk")
    my_list.insert(1,"kaju")
    return my_list

m=add_more_list(my_shopping_list)
print(m)
