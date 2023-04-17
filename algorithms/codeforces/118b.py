# https://codeforces.com/problemset/problem/118/B

n = int(input())
res = []

for i in range(n+1):
    # количество пробелов перед первой цифрой
    prefix = " " * ((n*2) - 2*i)
    for z in range(i+1):
        if z == 0:
            r = "0"
        else:
            r += f" {z}"
    tmp = r[:-1]
    res.append(prefix+r+tmp[::-1])

res += reversed(res[:-1])
for i in res:
    print(i)

