# https://codeforces.com/contest/1729/problem/B

def check(w):
    i = len(w) - 1
    res = []
    while i >= 0:
        if w[i] == '0':
            r = int(w[i-2:i])
            i -= 3
        else:
            r = int(w[i])
            i -= 1
        res.append(chr(ord('a') - 1 + r))
    return ''.join(res[::-1])

for _ in range(int(input())):
    input()
    print(check(input()))