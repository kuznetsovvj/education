# https://codeforces.com/problemset/problem/271/A

a = int(input())
while True:
    a = a + 1
    if len(set(str(a))) == 4:
        print(a)
        break