# https://codeforces.com/problemset/problem/1372/A

def check(n):
    res = [1 for i in range(n)]
    return ' '.join(map(str, res))

for _ in range(int(input())):
    print(check(int(input())))