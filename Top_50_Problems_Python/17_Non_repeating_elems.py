nums = list(map(int, input('Enter nums: ').split()))

singles = [i for i in nums if nums.count(i) == 1]

print(', '.join(map(str, singles)))