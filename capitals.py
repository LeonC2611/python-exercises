capitals = {"France": "Paris", "Japan": "Tokyo", "Egypt": "Cairo"}
capitals_correct = {}
#swaps the country to be the value and the capital to be the key in the empty dictionary
for country, capital in capitals.items():
    capitals_correct[capital] = country

print(capitals_correct)