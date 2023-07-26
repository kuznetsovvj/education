# https://codeforces.com/contest/1842/problem/A

for _ in range(int(input())):
    input()
    s1 = sum(map(int, input().split()))
    s2 = sum(map(int, input().split()))
    if s1 > s2:
        print("Tsondu")
    if s2 > s1:
        print("Tenzing")
    if s2 == s1:
        print("Draw")