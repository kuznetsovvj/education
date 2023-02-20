# https://codeforces.com/problemset/problem/1626/A

def check(word):
    s = {'1':set(), '2':set()}
    res = []
    for it in word:
        if it in s['1']:
            s['1'].remove(it)
            s['2'].add(it)
        else:
            s['1'].add(it)
    for z in s['2']:
        res.append(f"{z}{z}")
    for z in s['1']:
        res.append(z)
    return ''.join(res)


for _ in range(int(input())):
    print(check(input()))
