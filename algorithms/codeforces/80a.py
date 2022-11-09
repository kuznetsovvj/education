# https://codeforces.com/problemset/problem/80/A

def check_simple(x):
    for i in range(2, int(x**0.5)+2):
        if x % i == 0:
            return False
    return True

def solution(n, m):
    if not check_simple(m):
        return False
    for x in range(n + 1, m):
        if check_simple(x):
            return False
    return True

n, m = map(int, input().split())
if solution(n, m):
    print('YES')
else:
    print('NO')