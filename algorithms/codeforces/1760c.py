# https://codeforces.com/problemset/problem/1760/C

def check(seq):
    mx = [0, 0]
    for i in seq:
        if i > mx[0]:
            mx[1], mx[0] = mx[0], i
        elif i > mx[1]:
            mx[1] = i
    res = [0 for _ in range(len(seq))]
    for idx, item in enumerate(seq):
        if item != mx[0]:
            res[idx] = item - mx[0]
        else:
            res[idx] = item - mx[1]
    return ' '.join(map(str, res))


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))