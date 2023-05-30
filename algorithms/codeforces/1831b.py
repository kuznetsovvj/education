# https://codeforces.com/contest/1831/problem/B

from collections import defaultdict


def check(a, b):
    s_a = count(a)
    s_b = count(b)
    keys = list(s_a.keys()) + list(s_b.keys())
    m_ = 0
    for key in keys:
        m_ = max(m_, s_a[key] + s_b[key])
    return m_

def count(a):
    s = defaultdict(int)
    cnt_v, cnt_c = a[0], 0
    for idx, item in enumerate(a):
        if item == cnt_v:
            cnt_c += 1
        else:
            s[cnt_v] = max(s[cnt_v], cnt_c)
            cnt_v = item
            cnt_c = 1
    s[cnt_v] = max(s[cnt_v], cnt_c)
    return s


for _ in range(int(input())):
    input()
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    print(check(a, b))