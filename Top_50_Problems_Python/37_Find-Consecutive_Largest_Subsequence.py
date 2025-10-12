nums = list(map(int, input("Enter nums: ").split()))
length = len(nums)
totals = []
count = 0
for i in nums:
    n = 1
    while i + n in nums:
        n+=1
        count+=1
    totals.append(count + 1)
    count = 0

print(max(totals))
