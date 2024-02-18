# Формула Карндано

a, b, c, d = map(int, input().split())

p = (3*a*c - b*b) / (3*a*a)
q = (2*b*b*b - 9*a*b*c + 27*a*a*d) / (27*a*a*a)

dQ = (p / 3)**3 + (q / 2)**2

apl = ((-1)*q / 2 + dQ**0.5)
beta = ((-1)*q / 2 - dQ**0.5)
if apl < 0:
    apl = -((-apl)**(1./3.))
else:
    apl = apl**(1./3.)
if beta < 0:
    beta = -((-beta)**(1./3.))
else:
    beta = beta**(1./3.)
y = apl + beta
x = y - (b / (3*a))
print(x)