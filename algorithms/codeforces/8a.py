# https://codeforces.com/problemset/problem/8/A
# Количество попыток: 3 (ошибка в логике, исправленная со второго раза)
# Сложность 1200

def check(w, s1, s2):
    k = w.find(s1)
    if k == -1:
        return False
    k = w.find(s2, k + len(s1))
    if k == -1:
        return False
    return True

def solution(w, s1, s2):
    f = check(w, s1, s2)
    b = check(w[::-1], s1, s2)
        
    if b and f:
        return "both"
    if b:
        return "backward"
    if f:
        return "forward"
    return "fantasy"


w = input().strip()
s1 = input().strip()
s2 = input().strip()
print(solution(w, s1, s2))