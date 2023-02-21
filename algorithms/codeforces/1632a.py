# https://codeforces.com/problemset/problem/1632/A

def check(w):
    if len(w) >= 3:
        return "NO"
    if len(w) == 1:
        return "YES"
    if w[0] == w[1]:
        return "NO"
    return "YES"

for _ in range(int(input())):
    input()
    print(check(input()))