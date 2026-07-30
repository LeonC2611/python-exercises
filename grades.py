scores = {
    "Alice" : 92,
    "Bob" : 78,
    "Charlie" : 65,
    "Dana" : 50
}


for name in scores:
    if 100 >= scores[name] >= 90:
        print(f"{name}: {scores[name]} - A")
    elif 89 >= scores[name] >= 80:
        print(f"{name}: {scores[name]} - B")
    elif 79 >= scores[name] >= 70:
        print(f"{name}: {scores[name]} - C")
    elif 69 >= scores[name] >= 60:
        print(f"{name}: {scores[name]} - D")
    elif 59 >= scores[name] >= 0:
        print(f"{name}: {scores[name]} - F")

        