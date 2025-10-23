nums = list(map(int, input('Nums: ').split()))
num = int(input('Num: '))
nums.append(num)
final = sorted(nums.copy())

print(final.index(num))
