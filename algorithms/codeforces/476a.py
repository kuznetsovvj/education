# https://codeforces.com/problemset/problem/476/A

n, m = map(int, input().split())

if n < m:
    print(-1)
else:
    b, a = n // 2, n % 2

    while b >= 0 and (b + a) % m != 0:
        b -= 1
        a += 2  

    if (b + a) % m == 0:
        print(b + a)
    else:
        print(-1)