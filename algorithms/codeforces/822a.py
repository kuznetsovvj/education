# https://codeforces.com/problemset/problem/822/A

import math

a, b = map(int, input().split())
print(math.factorial(min(a, b)))