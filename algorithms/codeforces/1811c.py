# https://codeforces.com/contest/1811/problem/C
 
def check(seq):
    m = min(seq)
    fl = False
    res = [0 for _ in range(len(seq) + 1)]
    res[0] = seq[0]
    res[-1] = seq[-1]
    for i in range(1, len(seq)):
        res[i] = min(seq[i-1], seq[i])
    return ' '.join(map(str, res))
 
 
for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))