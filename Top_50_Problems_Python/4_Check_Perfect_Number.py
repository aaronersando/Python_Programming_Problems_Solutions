n = int(input("Enter n: "))

def getalldivs(n):
    nums = []
    for i in range(1,n):
        if n%i==0:
            nums.append(i)
    return nums

print("Perfect num") if sum(getalldivs(n)) == n else print("Not perfect num")
