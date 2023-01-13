# https://codeforces.com/problemset/problem/978/B


input()
cnt, res = 0, 0
for i in input():
    if i == 'x':
        cnt += 1
        if cnt >= 3:
            res += 1
    else:
        cnt = 0
print(res)