# https://codeforces.com/problemset/problem/1325/B

def check(s):
    return len(set(s))

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))