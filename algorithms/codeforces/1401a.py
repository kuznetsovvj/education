# https://codeforces.com/problemset/problem/1401/A

def check(n, k):
    if n < k:
        return k - n
    if n % 2 == k % 2:
        return 0
    return 1

for _ in range(int(input())):
    print(check(*map(int, input().split())))
