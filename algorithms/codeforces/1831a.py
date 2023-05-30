# https://codeforces.com/contest/1831/problem/A

def check(t):
    res = [0 for _ in range(len(t))]
    for i in range(len(t)):
        res[i] = len(t) - t[i] + 1
    return ' '.join(map(str, res))
    

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))