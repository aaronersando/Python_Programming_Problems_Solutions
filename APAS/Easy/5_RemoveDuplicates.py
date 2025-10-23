nums = sorted(list(map(int, input('Nums: ').split())))
unqs = sorted(list(set(nums)))
print(f'Len: {len(unqs)} \nUniques: {unqs}')