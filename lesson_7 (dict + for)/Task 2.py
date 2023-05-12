dict_stock={"banana": 6,"apple": 0,"orange": 32, "pear": 15}
dict_price={"banana": 4, "apple": 2, "orange": 1.5,"pear": 3}
total_price=0
for i in dict_price:
    if i in dict_stock:
        price=dict_price[i]
        stock=dict_stock[i]
        total_price += price*stock
print("Total price: ", total_price)



