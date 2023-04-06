# https://codeforces.com/contest/1811/problem/A
 
def check(w, t):
    for i in range(len(w)):
        if int(w[i]) < t:
            return w[:i] + str(t) + w[i:]
    return w + str(t)
 
for _ in range(int(input())):
    _, t = map(int, input().split())
    w = input()
    print(check(w, t))