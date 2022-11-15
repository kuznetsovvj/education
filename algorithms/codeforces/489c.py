# https://codeforces.com/problemset/problem/489/C

import copy


def check(c, s):
    # Если s < 1 или s > c * 9 - то решений точно нет
    if s > 9 * c:
        return "-1 -1"
    
    if s == 0 and c == 1:
        return "0 0"
    
    if s == 0:
        return "-1 -1"
    
    k = copy.copy(s)
    mn = [0 for _ in range(c)]
    for i in range(c-1, -1, -1):
        if s > 1:
            if i != 0:
                mn[i] = min(9, s - 1)
                s -= mn[i]
            else:
                mn[i] = s
        else:
            if i != 0:
                continue
            else:
                mn[0] = s

    mx = [0 for _ in range(c)]
    for i in range(c):
        mx[i] = min(9, k)
        k -= mx[i]
    
    return f"{''.join(map(str, mn))} {''.join(map(str, mx))}"
    

print(check(*map(int, input().split())))