# https://codeforces.com/problemset/problem/702/A

def check(seq):
    m, c = 1, 1
    for i in range(1,len(seq)):
        if seq[i] > seq[i-1]:
            c += 1
        else:
            m = max(m, c)
            c = 1
    m = max(m, c)
    return m


input()
seq = tuple(map(int, input().split()))
print(check(seq))