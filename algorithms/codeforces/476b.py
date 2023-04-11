# https://codeforces.com/problemset/problem/476/B

w1 = input()

r = 0
for i in w1:
    if i == '+':
        r += 1
    else:
        r -= 1

c = [0] * 21
c[10] = 1
w2 = input()
for idx, item in enumerate(w2):
    tmp = [0] * 21
    if item == '+':
        for i in range(len(c)):
            if c[i] != 0:
                tmp[i+1] += c[i]
    if item == '-':
        for i in range(len(c)):
            if c[i] != 0:
                tmp[i-1] += c[i]
    if item == '?':
        for i in range(len(c)):
            if c[i] != 0:
                tmp[i-1] += c[i] / 2
                tmp[i+1] += c[i] / 2
    c = tmp
print(c[r+10])