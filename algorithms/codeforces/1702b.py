# https://codeforces.com/problemset/problem/1702/B

def check(w):
    z = set()
    res = 1
    for i in w:
        if i in z:
            continue
        # i not in z
        if len(z) == 3:
            res += 1
            z.clear()
        z.add(i)
    return res

for _ in range(int(input())):
    print(check(input()))