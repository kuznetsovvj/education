# https://codeforces.com/contest/1915/problem/A

from collections import Counter

for _ in range(int(input())):
    s = Counter(map(int, input().split()))
    print(s.most_common()[1][0])
