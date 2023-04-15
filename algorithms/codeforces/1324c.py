# https://codeforces.com/problemset/problem/1324/C

def check(w):
    mx, cnt = 0, 0
    for i in w:
        if i == 'L':
            cnt += 1
        else:
            mx = max(mx, cnt)
            cnt = 0
    mx = max(mx, cnt)
    return mx + 1


for _ in range(int(input())):
    print(check(input()))