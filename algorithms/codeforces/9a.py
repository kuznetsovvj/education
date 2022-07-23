# https://codeforces.com/problemset/problem/9/A

def solution(a):
    if a == 6:
        return "1/6"
    if a == 5:
        return "1/3"
    if a == 4:
        return "1/2"
    if a == 3:
        return "2/3"
    if a == 2:
        return "5/6"
    if a == 1:
        return "1/1"


a, b = map(int, input().strip().split())
print(solution(max(a, b)))