# https://codeforces.com/problemset/problem/265/A

w = input().strip()
t = input().strip()

w_p, t_p = 0, 0
while t_p != len(t):
    if w[w_p] == t[t_p]:
        w_p += 1
    t_p += 1
    
print(w_p + 1)