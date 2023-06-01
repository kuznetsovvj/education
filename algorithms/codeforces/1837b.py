# https://codeforces.com/contest/1837/problem/B

def check(s):
    mx, crt = 1, 1
    t = s[0]
    for i in s[1:]:
        if i == t:
            crt += 1
        else:
            t = i
            crt = 1
        mx = max(mx, crt)
    return mx + 1


for _ in range(int(input())):
    input()
    print(check(input()))