str1= input("Enter word 1: ")
str2= input("Enter word 2: ")
rev1 = "".join(sorted(list(str1)))
rev2 = "".join(sorted(list(str2)))

if rev1 == rev2:
    print("Anagram")
else:
    print("Not Anagram")



