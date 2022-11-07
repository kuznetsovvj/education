# https://codeforces.com/contest/1703/problem/B

def check(w):
    s, res = set(), 0
    for item in w:
        if item not in s:
            res += 1
            s.add(item)
        res += 1
    return res

for _ in range(int(input())):
    input()
    print(check(input()))