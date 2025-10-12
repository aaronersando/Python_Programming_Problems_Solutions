str1 = input("enter str1: ")
str2 = input("enter str2: ")
# ? = 0, * = 1

str1c = str1.count('?')
new1 = "".join(str1.replace('?', '_'))  
new2 = "".join(str2.replace('*', '_'*str1c)) 

print("Match") if new1 == new2 else print("Not match")
print(new1)
print(new2)
