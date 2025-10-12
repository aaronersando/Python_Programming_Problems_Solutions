num = input("Enter number: ")
total = 0
for i in num:
    total += int(i) ** 3

print("Not armstrong") if total != int(num) else print("Armstrong")