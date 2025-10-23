words = input('Words: ').split()
ltrs = ''
smlst = min(words, key=len)
# print(smlst)
for i in range(len(smlst)-1):
    total = 0
    for j in words:
        if j[i] == smlst[i]:
            total += 1
    if total == len(words):
        ltrs += smlst[i]

print(ltrs) if ltrs else print('There is no common prefix among the input strings')