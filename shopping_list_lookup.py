prices = {"apple": 0.50, "bread": 2.00, "milk": 1.50}

while True:
    try:
        item = input("Please search for an item for it's price: ")
        print(f"£{prices[item]}")
        break
    except KeyError: # Instead of using pass, returned a message back to user and started loop again.
        print("Item not found")