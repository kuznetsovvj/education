# https://codeforces.com/contest/1851/problem/A

def check(m, k, H, seq):
    res = 0
    for item in seq:
        diff = abs(item - H)
        # сложно перефразировать условие, чтобы они оба стояли на эскалаторе
        if diff % k == 0 and min(item, H) + m * k > max(item, H) and item != H:
            res += 1
    return res


assert check(3, 3, 11, [5, 4, 14, 18, 2]) == 2

for _ in range(int(input())):
    _, m, k, H = map(int, input().split())
    seq = tuple(map(int, input().split()))
    print(check(m, k, H, seq))
