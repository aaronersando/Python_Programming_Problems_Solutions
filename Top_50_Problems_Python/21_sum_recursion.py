num = int(input("Enter num: "))

def recurSum(num):
    if num == 1:
        return num
    return num + recurSum(num-1)

print(recurSum(num))