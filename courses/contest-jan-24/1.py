def check(x,y):
    r = (x**2 + y**2)**0.5
    if r <= 0.1:
        return 3
    if r <= 0.8:
        return 2
    if r <= 1:
        return 1
    return 0

s = 0
for _ in range(3):
    s += check(*map(float, input().split()))
print(s)