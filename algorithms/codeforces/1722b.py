# https://codeforces.com/contest/1722/problem/B

def check(w1, w2):
    for x1, x2 in zip(w1, w2):
        if (x1 == x2) or (x1 != 'R' and x2 != 'R'):
            continue
        return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    input()
    w1 = input()
    w2 = input()
    print(check(w1, w2))