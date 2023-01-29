# https://codeforces.com/problemset/problem/1691/A

def check(seq):
    od, ev = 0, 0
    for i in seq:
        if i % 2 == 0:
            od += 1
        else:
            ev += 1
    return min(od, ev)

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))
    