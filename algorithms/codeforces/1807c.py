# https://codeforces.com/contest/1807/problem/C

def check(wrd):
    on, zr = set(), set()
    for idx, item in enumerate(wrd):
        if idx % 2 == 0:
            if item in zr:
                return "NO"
            on.add(item)
        else:
            if item in on:
                return "NO"
            zr.add(item)
    return "YES"

for _ in range(int(input())):
    input()
    w = input()
    print(check(w))