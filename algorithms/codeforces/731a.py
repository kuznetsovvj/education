# https://codeforces.com/problemset/problem/731/A

def check(w):
    cnt = 0
    w = 'a' + w
    for i in range(1, len(w)):
        if w[i] == w[i-1]:
            continue
        if ord(w[i]) > ord(w[i-1]):
            cnt += min(122-ord(w[i])+ord(w[i-1])-97+1, ord(w[i])-ord(w[i-1]))
        else:
            cnt += min(122-ord(w[i-1])+ord(w[i])-97+1, ord(w[i-1])-ord(w[i]))
    return cnt

print(check(input()))