# https://codeforces.com/problemset/problem/1343/C

def check(seq):
    positive = seq[0] > 0
    cur_max = seq[0]
    res = 0
    for item in seq:
        if positive ^ (item > 0) == False:
            cur_max = max(cur_max, item)
        else:
            res += cur_max
            positive = item > 0
            cur_max = item
    res += cur_max
    return res

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))