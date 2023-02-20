# https://codeforces.com/problemset/problem/1629/A

def check(k, seq):
    seq.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(seq)):
        if seq[i][0] > k:
            return k
        k += seq[i][1]
    return k

for _ in range(int(input())):
    _, k = map(int, input().split())
    seq = list(zip(map(int, input().split()), map(int, input().split())))
    print(check(k, seq))