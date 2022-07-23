# https://codeforces.com/problemset/problem/189/A

x, a, b, c = map(int, input().split())
t = [a, b, c]
t.sort()
a, b, c = t

res = float('-inf')
xa, xb, xc = 0, 0, 0
while xc * c < x:
    if x % c == 0:
        res = max(res, x // c)
    xb = 0
    while xc * c + xb * b < x:
        if (x - (xc * c)) % b == 0:
            res = max(res, xc + ((x - xc*c) // b))

        if (x - (xc * c) - (xb * b)) % a == 0:
            xa = (x - (xc * c) - (xb * b)) // a
            res = max(res, xa + xb + xc)
        xb += 1
    xc += 1
print(res)