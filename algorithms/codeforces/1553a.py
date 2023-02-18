# https://codeforces.com/problemset/problem/1553/A

def check(x):
    return (x + 1) // 10

for _ in range(int(input())):
    print(check(int(input())))