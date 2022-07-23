#  https://codeforces.com/contest/1551/problem/A
#  сложность 800

import sys


def solution(k):
    num1, num2 = k // 3, k // 3
    if k % 3 == 1:
        num1 += 1
    if k % 3 == 2:
        num2 += 1
    return (num1, num2)


inp = [int(line) for line in sys.stdin]

for idx in range(1, len(inp)):
    print(' '.join(map(str, solution(inp[idx]))))