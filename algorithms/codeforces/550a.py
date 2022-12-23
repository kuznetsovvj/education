# https://codeforces.com/problemset/problem/550/A

def check(w):
    s, k = 0, 0
    r_a, r_b = set(), set()
    while k != -1:
        k = w.find('AB', s)
        if k != -1:
            s = k + 1
            r_a.add(s)
    
    s, k = 0, 0
    while k != -1:
        k = w.find('BA', s)
        if k != -1:
            s = k + 1
            r_b.add(s)

    if len(r_a) == 0 or len(r_b) == 0:
        return 'NO'

    if len(r_a) == 1 and len(r_b) == 1:
        a = r_a.pop()
        b = r_b.pop()
        if a == b - 1 or b == a - 1:
            return 'NO'

    if len(r_a) == 1:
        a = r_a.pop()
        if any([i for i in r_b if i != a +1 and i != a - 1]):
            return 'YES'
        else:
            return 'NO'

    if len(r_b) == 1:
        b = r_b.pop()
        if any([i for i in r_a if i != b +1 and i != b - 1]):
            return 'YES'
        else:
            return 'NO'
    
    return 'YES'

print(check(input()))