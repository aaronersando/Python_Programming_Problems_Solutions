n = int(input("Enter number: "))

f, s = 0, 1
next = 0
nums = [f, s]
        
for i in range(2,n):
    next = f + s
    f = s
    s = next
    nums.append(next)
        
print(nums)
        
