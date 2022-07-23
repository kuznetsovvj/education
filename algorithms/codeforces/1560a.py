# https://codeforces.com/contest/1560/problem/A
# сложность 800

import sys

# 1667 - более чем тысячный элемент последовательности по условию
seq = [i for i in range(1667) if i % 3 != 0 and i % 10 != 3]

inp = [int(r) for r in sys.stdin]

for idx in range(1, len(inp)):
    print(seq[inp[idx] - 1])