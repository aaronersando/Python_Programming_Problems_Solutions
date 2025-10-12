from collections import Counter

string = input('Enter string: ')
ldict = Counter(string)
singles = []

for i, j in ldict.items():
    if j == 1:
        singles.append(i)

print(', '.join(singles))