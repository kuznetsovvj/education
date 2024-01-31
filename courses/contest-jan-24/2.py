input()
mn, mx = float('inf'), float('-inf')
cn = 0
for i in input():
    if i == '#':
        mn = min(cn, mn)
        mx = max(cn, mx)
        cn = 0
    else:
        cn += 1

mn = min(mn, cn)
mx = max(mx, cn)
print(mn, mx)