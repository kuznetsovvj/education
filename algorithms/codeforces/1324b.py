# https://codeforces.com/problemset/problem/1324/B

from collections import defaultdict


def check(seq):
    st = set()
    s = defaultdict(int)
    st.add(seq[0])
    s[seq[0]] = 0
    for i in range(1, len(seq)):
        if seq[i] in st and i - s[seq[i]] != 1:
            return "YES"
        if seq[i] in st:
            continue
        st.add(seq[i])
        s[seq[i]] = i
    return "NO"

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))