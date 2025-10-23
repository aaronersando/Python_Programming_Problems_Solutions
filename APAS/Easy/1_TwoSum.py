nums = list(map(int, input('Nums: ').split()))
target = int(input('Target: '))
index = []

for i in range(len(nums)-1):
    for j in range(i, len(nums)-1):
        if nums[i] + nums[j] == target:
            index.append(i)
            index.append(i+j)

print(f'Indexes: {index}')
