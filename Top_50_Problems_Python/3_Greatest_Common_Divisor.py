n1 = int(input("n1: "))
n2 = int(input("n2: "))

def getalldivs(n):
    nums = []
    for i in range(1, n):
        if n%i==0:
            nums.append(i)
    return nums

divs1 = list(reversed(getalldivs(n1)))
divs2 = list(reversed(getalldivs(n2)))


gdc = 0

if len(divs1) < len(divs2):
    for i in divs1:
        if i in divs2:
            gdc = i
            break
else:
    for i in divs2:
        if i in divs1:
            gdc = i
            break

print(gdc)
        
