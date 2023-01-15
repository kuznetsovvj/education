# https://codeforces.com/problemset/problem/1476/A

def check(n, k):
    if k % n == 0:
        return k // n
    if k < n:
        if n % k == 0:
            return 1
        return 2
    return k // n + 1

for _ in range(int(input())):
    print(check(*map(int, input().split())))