# https://codeforces.com/contest/1851/problem/B

def check(seq):
    t1 = [i for i in seq if i % 2 == 1]
    t2 = [i for i in seq if i % 2 == 0]
    t1.sort()
    t2.sort()
    i1, i2 = 0, 0
    res = []
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            res.append(t2[i2])
            i2 += 1
        else:
            res.append(t1[i1])
            i1 += 1
    for i in range(1, len(seq)):
        if res[i] < res[i-1]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))
