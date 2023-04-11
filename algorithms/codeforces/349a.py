# https://codeforces.com/problemset/problem/349/A


def check(seq):
    s25, s50 = 0, 0
    for i in seq:
        if i == 25:
            s25 += 1
        if i == 50:
            if s25 == 0:
                return "NO"
            s25 -= 1
            s50 += 1
        if i == 100:
            if s50 >= 1 and s25 >= 1:
                s50 -= 1
                s25 -= 1
                continue
            if s50 == 0 and s25 >= 3:
                s25 -= 3
                continue
            return "NO"
    return "YES"


input()
print(check(tuple(map(int, input().split()))))
