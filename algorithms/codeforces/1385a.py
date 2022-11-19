# https://codeforces.com/problemset/problem/1385/A

from collections import Counter


def check(seq):
    x, y, z = seq
    if x != y and y != z and x != z:
        print("NO")
        return
    
    if x == y:
        if x < z:
            print("NO")
            return
        else:
            print("YES")
            print(f"{x} {z} {z}")
            return
    
    if y == z:
        if y < x:
            print("NO")
            return
        else:
            print("YES")
            print(f"{x} {x} {y}")
            return

    if x == z:
        if x < y:
            print("NO")
            return
        else:
            print("YES")
            print(f"{y} {x} {y}")
            return
    
"""
Можно сильно проще:
    a,b,c = sorted([a,b,c])
    if b != c:
        return 'NO'
    return 'YES\n'+str(a)+' '+str(a)+' '+str(c)
"""

for _ in range(int(input())):
    seq = tuple(map(int, input().split()))
    check(seq)