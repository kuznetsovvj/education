# https://codeforces.com/contest/1838/problem/D
 
# Решил после подсказки из разбора
import bisect
 
 
def check(w, req):
    # если последовательность
    if len(w) % 2 == 1:
        for _ in range(len(req)):
            print("NO")
        return
    
    a, s = list(), set()
    for idx, item in enumerate(w):
        if (idx + 1) % 2 == 0 and item == '(':
            a.append(idx+1)
            s.add(idx+1)
        if (idx + 1) % 2 == 1 and item == ')':
            a.append(idx+1)
            s.add(idx+1)
    
    for r in req:
        if r in s:
            t = bisect.bisect_left(a, r)
            del a[t]
            s.remove(r)
        else:
            bisect.insort_left(a, r)
            s.add(r)        
        if len(a) != 0 and (a[0] % 2 == 1 or a[-1] % 2 == 0):
            print("NO")
        else:
            print("YES")
 
 
_, t = map(int, input().split())
w = input()
r = []
for _ in range(t):
    r.append(int(input()))
check(w, r)
 