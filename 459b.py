# https://codeforces.com/problemset/problem/459/B

# на первой посылке потерял случай max(seq) = min(seq)

from collections import Counter


input()
seq = tuple(map(int, input().split()))
c = Counter(seq)
if max(seq) != min(seq):
    print(max(seq) - min(seq), c[max(seq)] * c[min(seq)])
else:
    print(0, c[seq[0]] * (c[seq[0]] - 1) // 2)