a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x = (-1*b + (b**2 - 4*a*c)**0.5)/(2*a)
y = (b + (b**2 - 4*a*c)**0.5)/(2*a)

print(f'The roots of this quadratic equation is: {x}, {y}')
