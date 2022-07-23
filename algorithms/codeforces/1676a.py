def sol(w):
    r1, r2 = 0, 0
    for z in range(len(w)):
        i = int(w[z])
        if z < 3:
            r1 += i
        else:
            r2 += i
    if r1 == r2:
        return "YES"
    return "NO"


t = int(input().strip())
for tt in range(t):
    print(sol(input().strip()))