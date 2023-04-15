# https://codeforces.com/problemset/problem/1721/A
 
from collections import defaultdict
 
 
def check(w):
    c = defaultdict(int)
    for i in w:
        c[i] += 1
    v = sorted(c.values(), reverse=True)
    v.pop()
    return len(v)
 
 
for _ in range(int(input())):
    w1 = input()
    w2 = input()
    print(check(w1+w2))