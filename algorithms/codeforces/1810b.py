#https://codeforces.com/contest/1810/problem/B

def check(n):
    if n % 2 == 0:
        print(-1)
        return
    res = []
    while n != 1:
        if ((n - 1) // 2) % 2 != 0:
            res.append(2)
            n = (n - 1) // 2
        else:
            res.append(1)
            n = (n + 1) // 2
        if len(res) >= 40:
            print(-1)
            return
    print(len(res))
    print(' '.join(map(str, res[::-1])))

for _ in range(int(input())):
    check(int(input()))