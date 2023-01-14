# https://codeforces.com/problemset/problem/686/A

import sys

inp = [line.strip() for line in sys.stdin]
_, x = map(int, inp[0].split())
t = 0

for line in inp[1:]:
    op, value = line.split()
    if op == '+':
        x += int(value)
    else:
        if x >= int(value):
            x -= int(value)
        else:
            t += 1
print(f"{x} {t}")
