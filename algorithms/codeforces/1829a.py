# https://codeforces.com/contest/1829/problem/A

def check(w):
    template = "codeforces"
    res = 0
    for i in range(len(template)):
        if template[i] != w[i]:
            res += 1
    return res

for _ in range(int(input())):
    print(check(input()))
