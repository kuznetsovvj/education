# https://codeforces.com/problemset/problem/1303/A

def check(w):
    r = 0
    for i in w:
        if i == '0':
            r += 1
    return r

for _ in range(int(input())):
    print(check(input().strip('0')))
