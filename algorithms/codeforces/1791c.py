# https://codeforces.com/contest/1791/problem/C

def check(s):
    res = len(s)
    for i in range(len(s) // 2):
        if i < len(s) - 1 - i and s[i] != s[-1 - i]:
            res -= 2
        else:
            return res
    return res

for _ in range(int(input())):
    input()
    print(check(input().strip()))