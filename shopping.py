
inventory = {
    "apple" : 3,
    "banana" : 2,
    "pear" : 1
}
# Using True as an argument in the loop, forces user to manually break the loop, will continue to ask for item to buy otherwise or display out of stock if everything is gone.
while True:
    item = input("What would you like to buy? (Apple. Banana, Pear) ")
    item = item.lower()
    if item == "quit":
        break
    if item not in inventory:
        print("Not a recognised item")
    elif inventory[item] == 0:
        print(f"{item.capitalize()}s are out of stock.")
    else:
        inventory[item] -= 1
        print(f"Stock: {inventory[item]}")
        
        
        
    