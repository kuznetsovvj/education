# https://codeforces.com/problemset/problem/1759/A

def check(w):
    ptr = "Yes" * (len(w) // 3 + 3)
    start = -1
    for i in range(3):
        if w[0] == ptr[i]:
            start = i
    if start == -1:
        return "NO"
    t = 0
    while t < len(w):
        if w[t] != ptr[start+t]:
            return "NO"
        t += 1
    return "YES"

for _ in range(int(input())):
    print(check(input()))