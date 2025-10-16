num = int(input('Enter num: '))
primes = []

while num%2 == 0:
    if num%2 == 0:
        primes.append(2)
        num /= 2
primes.append(int(num))

print(primes)
        