# https://codeforces.com/contest/1915/problem/B

for _ in range(int(input())):
    for _ in range(3):
        s = {'A', 'B', 'C', '?'}
        w = input()
        for item in w:
            s.remove(item)
        if '?' not in s:
            print(s.pop())

