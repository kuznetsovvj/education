import sys

def query(x):
    print(x)
    sys.stdout.flush()
    return input()

n = int(input())

mn, mx = 1, n + 1

while (mx - mn) > 1:
    t = (mx + mn) // 2
    #print(mx, mn)
    res = query(t)
    if res == '<':
        mx = t
    else:
        mn = t

print(f"! {mn}")
