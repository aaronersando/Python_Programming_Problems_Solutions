num1, den1 = map(int, input("Enter num 1 fraction: ").split('/'))
num2, den2 = map(int, input("Enter num 2 fraction: ").split('/'))

n = (num1*den2) + (num2*den1)
d = (den1 * den2)

gcd = 0
for i in range(1, min(n, d) + 1):
    if n%i == 0 and d%i==0:
        gcd = i

print(f'The answer is: {int(n/gcd)}/{int(d/gcd)}')