# https://codeforces.com/problemset/problem/1480/A

def check(w):
    res = []
    for idx, item in enumerate(w):
        if idx % 2 == 0:
            if item == 'a':
                res.append('b')
            else:
                res.append('a')
        else:
            if item == 'z':
                res.append('y')
            else:
                res.append('z')
    return ''.join(map(str, res))

for _ in range(int(input())):
    print(check(input()))