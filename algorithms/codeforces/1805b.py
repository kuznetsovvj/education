# https://codeforces.com/contest/1805/problem/B

def check(word):
    m = ord('z')
    idx = len(word) - 1
    for i in range(len(word)-1, 0, -1):
        if ord(word[i]) < m:
            m = ord(word[i])
            idx = i
    if m <= ord(word[0]):
        return word[idx] + word[:idx] + word[idx+1:]
    return word


for _ in range(int(input())):
    input()
    w = input()
    print(check(w))