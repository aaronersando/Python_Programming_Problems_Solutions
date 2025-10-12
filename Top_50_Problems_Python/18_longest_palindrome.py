words = input("Enter words: ").split()
words.sort(key=len, reverse=True)

for i in words:
    if i == i[::-1]:
        print(i)
        break



