from collections import Counter

word = input("Enter word: ")
counts = Counter(word)
print(counts)

for letter, count in counts.items():
    print(letter + " appears " + str(count) + " time")
