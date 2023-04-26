# https://codeforces.com/problemset/problem/1324/A
 
def check(seq):
    s = set()
    for i in seq:
        s.add(i % 2)
    if len(s) == 1:
        return "YES"
    return "NO"
 
 
for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))