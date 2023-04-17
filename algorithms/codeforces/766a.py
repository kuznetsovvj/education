# https://codeforces.com/problemset/problem/766/A

def check(w1, w2):
    if w1 != w2:
        return max(len(w1), len(w2))
    return -1 

w1 = input()
w2 = input()
print(check(w1, w2))