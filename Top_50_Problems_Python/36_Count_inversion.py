nums = list(map(int, input("Enter nums: ").split()))
length = len(nums)
total = 0
for i in range(length):
    for j in range(i + 1, length):
        if nums[j] < nums[i]:
            total += 1
print(f'Total inversions count: {total}')
