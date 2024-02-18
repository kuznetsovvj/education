n = float(input())

def calc(x, n):
    r = x**2 + (x + 1)**0.5
    return n - r

low, high = -1, n**0.5
candidate = (low + high) / 2
z = calc(candidate, n)
while abs(z) > 0.000001:
    if z > 0:
        low = candidate
    else:
        high = candidate
    candidate = (low + high) / 2
    z = calc(candidate, n)

print(candidate)

