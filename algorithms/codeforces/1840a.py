# https://codeforces.com/contest/1840/problem/A

def check(w):
    res, prev = [], ""
    for i in w:
        if prev == "":
            prev = i
            res.append(i)
            continue
        if i == prev:
            prev = ""
    return ''.join(res)


for _ in range(int(input())):
    input()
    print(check(input()))