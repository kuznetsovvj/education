# https://codeforces.com/problemset/problem/1509/A
 
def check(seq):
    a, b = [], []
    for i in seq:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    return " ".join(map(str, a + b))
 
for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))