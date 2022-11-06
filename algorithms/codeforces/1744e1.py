# https://codeforces.com/contest/1744/problem/E1
# https://codeforces.com/contest/1744/problem/E2

import math


def div(num):
    res = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res.append(i)
            if i != num // i:
                res.append(num // i)
    return res

# неверно...
def check(seq):
    a, b, c, d = seq
    div_a, div_b = div(a), div(b)
    
    # переберем все возможные пары делителей a и b
    for item_a in div_a:
        for item_b in div_b:
            v1 = item_a * item_b
            v2 = a * b // v1
            x = (c // v1) * v1
            y = (d // v2) * v2

            if x > a and y > b:
                return f"{x} {y}"
    
    return "-1 -1"


t = int(input())
for _ in range(t):
    seq = tuple(map(int, input().split()))
    print(check(seq))