# https://codeforces.com/contest/1538/problem/C

from collections import defaultdict
import sys

def solution(a, b, k):
    div_a = divisors(a)
    div_b = divisors(b)
    keys = set(div_a.keys) + set(div_b.keys())
    res = 0
    for key in keys:
        res += abs(div_a[key] - div_b[key])
    if res > k:
        return "NO"
    else:
        return "YES"


def divisors(n):
    res = defaultdict(int)
    d = 2
    while d**2 <= n:
        if n % d == 0:
            res[d] += 1
            n //= d
        else:
            d += 1
    if n > 1:
        res[d] += 1
    return res

assert(solution(36, 48, 2)) == "YES"
assert(solution(36, 48, 3)) == "YES"
assert(solution(36, 48, 4)) == "YES"
assert(solution(2, 8, 1)) == "YES"
assert(solution(2, 8, 2)) == "YES"
assert(solution(1000000000, 1000000000, 1000000000)) == "NO"
assert(solution(1, 2, 1)) == "YES"
assert(solution(2, 2, 1)) == "NO"

"""
input_ = (tuple(map(int, line.strip().split())) for line in sys.stdin)
n, _ = next(input_)
for j in range(n):
    a, b, k = next(input_)
    print(solution(a, b, k))
    """

