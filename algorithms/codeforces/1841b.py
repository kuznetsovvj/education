# https://codeforces.com/contest/1841/problem/B

def check(seq):
    cr_min, cr_max, sortmode = seq[0], seq[0], True
    prev = -1
    res = [1]
    for i in range(1, len(seq)):
        if sortmode:
            if seq[i] >= cr_max:
                res.append(1)
                cr_max = seq[i]
            elif seq[i] <= cr_min:
                res.append(1)
                sortmode = False
                prev = seq[i]
            else:
                res.append(0)
        else:
            if seq[i] >= prev and seq[i] <= cr_min:
                res.append(1)
                prev = seq[i]
            else:
                res.append(0)
    return ''.join(map(str, res))


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))