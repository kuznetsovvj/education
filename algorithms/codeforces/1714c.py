# https://codeforces.com/contest/1714/problem/C

def check(num):
    t = {i for i in range(1, 10)}
    res = set()
    while num != 0:
        if num >= 10:
            s = max(t)
            num -= s
            res.add(s)
            t.remove(s)
        else:
            k = num
            while True:
                if k in t:
                    res.add(k)
                    t.remove(k)
                    num -= k
                    break
                else:
                    k -= 1
    res = list(res)
    res.sort()
    return ''.join(map(str, res))


t = int(input())
for _ in range(t):
    s = int(input())
    print(check(s))