# https://codeforces.com/problemset/problem/1327/A

def check(n, k):
    if (n % 2 == 0) ^ (k % 2 == 0):
        return "NO"
    if (n < k **2 ):
        return "NO"
    return "YES"

for _ in range(int(input())):
    print(check(*map(int, input().split())))