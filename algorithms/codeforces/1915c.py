# https://codeforces.com/contest/1915/problem/C

for _ in range(int(input())):
    input()
    s = sum(list(map(int, input().split())))
    if (int(s**0.5))**2 == s:
        print("YES")
    else:
        print("NO")