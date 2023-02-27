# https://codeforces.com/problemset/problem/1490/C

def check(n):
    # проверяем все делители n
    m = set([1, n])
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            m.add(i)
            m.add(n // i)

    for d in m:
        if (d**2 - (n // d)) % 3 != 0:
            continue
            
        p = (d**2 - (n // d)) // 3
        if p <= 0:
            continue
        
        #print(f"a*b={p}, a+b={d}")

        ds = d**2 - 4*p
        if ds < 0:
            continue

        if int(ds**0.5) != float(ds**0.5):
            continue

        x0 = (d + ds**0.5) // 2
        x1 = (d - ds**0.5) // 2

        #print(f"x1: {x1}, x2: {x0}")

        if int(x0) != float(x0) or int(x1) != float(x1):
            continue
        
        return "YES"

    return "NO"

for _ in range(int(input())):
    print(check(int(input())))