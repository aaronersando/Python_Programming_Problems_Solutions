nums = list(map(int, input("Enter nums: ").split()))
numsSorted = sorted(nums.copy())
# print(numsSorted)
finalRank = []
for j in nums: 
    for idx, item in enumerate(numsSorted):
        if item == j:
            finalRank.append(idx+1)

print(finalRank)