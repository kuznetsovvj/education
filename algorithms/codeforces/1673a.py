# https://codeforces.com/problemset/problem/1673/A

def sol(w):
    if len(w) % 2 == 0:
        return f"Alice {cnt(w)}"
    else:
        if len(w) == 1:
            return f"Bob {cnt(w)}"
        else:
            m = max(cnt(w[1:]) - cnt(w[0]), cnt(w[:-1]) - cnt(w[-1]))
            return f"Alice {m}"
    
def cnt(w):
    s = 0
    for i in range(len(w)):
        s += ord(w[i]) - ord('a') + 1
    return s

t = int(input())
for tt in range(t):
    print(sol(input()))