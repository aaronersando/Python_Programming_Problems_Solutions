num = (input("Num: "))

revNum = num[::-1] if '-' not in num else '-' + num[:0:-1]
print(revNum)
    