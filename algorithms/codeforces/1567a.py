# https://codeforces.com/problemset/problem/1567/A

def check(s):
    res = []
    for it in s:
        if it == 'U':
            res.append('D')
        elif it == 'D':
            res.append('U')
        else:
            res.append(it)
    return ''.join(res)

for _ in range(int(input())):
    input()
    print(check(input().strip()))
