# https://codeforces.com/problemset/problem/10/A

def sol(n, p1, p2, p3, t1, t2, seq):
    res = 0
    for i in range(len(seq)):
        if i != 0:
            delta = seq[i][0] - seq[i-1][1]
            if delta < t1:
                res += delta * p1

            else:
                res += t1 * p1
                delta -= t1
            
                if delta < t2:
                    res += delta * p2
                else:
                    res += t2 * p2
                    delta -= t2
                    res += delta * p3

        res += (seq[i][1] - seq[i][0]) * p1
    return res

n, p1, p2, p3, t1, t2 = map(int, input().strip().split())
seq = []
for nn in range(n):
    seq.append(tuple(map(int, input().strip().split())))
print(sol(n, p1, p2, p3, t1, t2, seq))

