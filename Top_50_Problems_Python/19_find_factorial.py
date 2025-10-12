num = int(input("Enter num: "))

def fact(num):
    if num == 1:
        return num
    elif num == 0:
        return 1
    else:
        return num * fact(num-1) 

print(fact(num))