# https://codeforces.com/problemset/problem/1790/A
 
t = "314159265358979323846264338327"
 
def check(w):
    r = 0
    for i in range(len(w)):
        if w[i] == t[i]:
            r += 1
        else:
            return r
    return r
 
for _ in range(int(input())):
    print(check(input()))