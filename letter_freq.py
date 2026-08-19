import sys
letter_count = {}
for letter in sys.argv[1].lower():
    if letter not in letter_count:
        letter_count[letter] = 1
    else:
        letter_count[letter] += 1
letter_count = dict(sorted(letter_count.items()))

for letters in letter_count:
    print(f"# {letters}: {letter_count[letters]} ")