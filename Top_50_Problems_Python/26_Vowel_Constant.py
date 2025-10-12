char = input("Enter char: ")

if char in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
    print("Vowel")
elif char.isalpha():
    print('Consonant')
else:
    print('Neither Vowel or consonant')