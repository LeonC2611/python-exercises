sentence = input("Sentence = ")
sentence = sentence.split()
word_counts = {}
#loops through each word that was separated in sentence variable
for word in sentence:
# adds 1 if the word is already in word_count dictionary
    if word in word_counts:
        word_counts[word] += 1
#if word isn't in word_count dictionary, adds it and assigns it the score of 1
    else:
        word_counts[word] = 1

print(word_counts)
