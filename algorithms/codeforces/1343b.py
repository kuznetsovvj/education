# https://codeforces.com/problemset/problem/1343/B

def check(n):
    if (n // 2) % 2 == 1:
        print('NO')
    else:
        a = [i*2 for i in range(1, n // 2 + 1)]
        b = [2*i+1 for i in range(0, n // 2 - 1)]
        res = a + b + [sum(a) - sum(b)]
        print('YES')
        print(' '.join(map(str, res)))


t = int(input())
for _ in range(t):
    check(int(input()))