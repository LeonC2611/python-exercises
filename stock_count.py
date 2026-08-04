day1 = {"apple": 5, "banana": 3}
day2 = {"apple": 2, "banana": 4, "pear": 1}
total_stock = {}
# Adds all new items to the new dictionary
for fruit, stock in day1.items():
    if fruit not in total_stock:
        total_stock[fruit] = stock
# Adds stock count onto any existing item's stock count if it already exists in the new dictionary. Adds new items 
for fruit, stock in day2.items():
    if fruit in total_stock:
        total_stock[fruit] += stock
    else:
        total_stock[fruit] = stock


print(total_stock)