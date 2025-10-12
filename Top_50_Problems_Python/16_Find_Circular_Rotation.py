array = input("Enter elems: ").split()
k = int(input("Enter num: "))

for i in range(k):
    num = array.pop()
    array.insert(0, num)

print(array)