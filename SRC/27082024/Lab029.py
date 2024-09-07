def make_pizza(*toppings):
    print(toppings)
pramod=make_pizza("tomato")
dhir=make_pizza("olives","paneer","sweet")

def make_pizza(*toppings,base):
    print(toppings, base)
make_pizza("tomatoo","corn","cheese",base="crust")