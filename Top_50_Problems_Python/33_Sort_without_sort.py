x = list(map(int, input('Enter nums: ').split()))
nums = len(x)
for i in range(nums-1):
    for j in range(nums-i-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print(x)