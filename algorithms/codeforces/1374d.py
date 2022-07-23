from collections import defaultdict

inp = int(input())
for _ in range(inp):
    n, k = tuple(map(int, input().split()))
    ddict = defaultdict(int)
    seq = tuple(map(int, input().split()))
    for item in seq:
        ddict[item % k] += 1
    ddict[0] = 0
    value_max = float('-inf')
    for key, value in ddict.items():
        if value > value_max:
            value_max = value
            key_max = key
        if value == value_max and key < key_max:
            key_max = key

    if value_max == 0:
        print(0)
    else:
        print(value_max * k - key_max + 1)
    