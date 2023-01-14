# https://codeforces.com/problemset/problem/1760/B

def check(word):
    m = 0
    for i in word:
        m = max(m, ord(i) - ord('a') + 1)
    return m

for _ in range(int(input())):
    input()
    print(check(input()))