# https://codeforces.com/problemset/problem/4/A

def solution(n):
    if n % 2 != 0 or n == 2:
        return "NO"
    return "YES"


print(solution(int(input())))