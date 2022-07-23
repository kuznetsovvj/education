# https://codeforces.com/contest/1676/problem/F

from collections import Counter
 
def sol(k, seq):
    c = Counter(seq)
    mx = 0
    m_l, m_r = 0, 0
    keys = [i for i in sorted(c.keys()) if c[i] >= k]
    if len(keys) == 0:
        return "-1"
    s = [keys[0]]
    for z in range(1, len(keys)):
        if keys[z] != keys[z-1] + 1:
            if len(s) - 1 >= mx:
                mx = len(s) - 1
                m_l, m_r = s[0], s[-1]
            s.clear()
        s.append(keys[z])
    if len(s) - 1 >= mx:
        mx = len(s) - 1
        m_l, m_r = s[0], s[-1]

    if not m_l and not m_r:
        return "-1"
    return f"{m_l} {m_r}"
 
 
t = int(input().strip())
for tt in range(t):
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    print(sol(k, seq))