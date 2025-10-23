haystack = input('Haystack: ')
needle = input('Needle: ')
n = len(haystack)
k = len(needle)

final = ''
for i in range(n - k + 1):
    if needle == haystack[i:i+k]:
        final = str(i)
        break

print('None') if not needle or not final else print(final)