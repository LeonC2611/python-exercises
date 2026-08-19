# Using import function to import sys module
import sys
letter_count = {}
# This loop iterates through the command line argument word to add letters to a dictionary and assign a number based on how many times the letter appeared in the word.
for letter in sys.argv[1].lower():
    if letter not in letter_count:
        letter_count[letter] = 1
    else:
        letter_count[letter] += 1
letter_count = dict(sorted(letter_count.items()))
# This loop iterates through the newly sorted dictionary and prints the letters with how many times they appear in the word in alphabetical order.
for letters in letter_count:
    print(f"# {letters}: {letter_count[letters]} ")