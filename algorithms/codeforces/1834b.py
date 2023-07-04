# https://codeforces.com/contest/1834/problem/B

def check(mn, mx):
    mn_c, mx_c = mn % 10, mx % 10
    mn, mx = mn // 10, mx // 10
    res = 0
    while mn != 0 or mx != 0:
        if mn != mx:
            res += 9
        else:
            res += abs(mn_c - mx_c)
        mn_c, mx_c = mn % 10, mx % 10
        mn, mx = mn // 10, mx // 10
    res += abs(mn_c - mx_c)
    return res        


for _ in range(int(input())):
    print(check(*map(int, input().split())))