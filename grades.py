scores = {
    "Alice" : 92,
    "Bob" : 78,
    "Charlie" : 65,
    "Dana" : 50
}

#.items() grabs both key and value and stores them both in variables (name & score). Better to use than each dictionary lookup for each conditional. This time just refers back to variable.
for name, score in scores.items():
    if 100 >= score >= 90:
        print(f"{name}: {score} - A")
    elif 89 >= score >= 80:
        print(f"{name}: {score} - B")
    elif 79 >= score >= 70:
        print(f"{name}: {score} - C")
    elif 69 >= score >= 60:
        print(f"{name}: {score} - D")
    elif 59 >= score >= 0:
        print(f"{name}: {score} - F")

        