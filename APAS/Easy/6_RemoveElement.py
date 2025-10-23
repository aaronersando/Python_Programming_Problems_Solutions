nums = list(map(int, input('Nums: ').split()))
val =  int(input("Val: "))
final = [x for x in nums if x != val]
print(f'Len: {len(final)} \nValues: {final}')