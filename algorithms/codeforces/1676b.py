def sol(seq):
    mn = min(seq)
    res = 0
    for item in seq:
        res += item - mn
    return res

t = int(input().strip())
for tt in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(sol(seq))