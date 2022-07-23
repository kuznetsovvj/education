# https://codeforces.com/problemset/problem/9/B
# Сложность 1200
# Количество попыток 2 (не учел условие, что делать при равенстве)

def solution(vb, vs, ux, uy, stops):
    tmin, res = float('inf'), -1
    prev = float('inf')
    for i in range(1, len(stops)):
        t = stops[i] / vb + (abs(ux - stops[i])**2 + uy**2)**0.5 / vs
        if t < tmin:
            tmin, res = t, i
            s = (abs(ux - stops[i])**2 + uy**2)**0.5
        # костыль для равенства
        if t == tmin:
            s_current = (abs(ux - stops[i])**2 + uy**2)**0.5
            if s_current < s:
                tmin, res, s = t, i, (abs(ux - stops[i])**2 + uy**2)**0.5
        if t > prev:
            break # если время пути начало расти, смысла обсчитывать дальше уже нет
        prev = t
    return res + 1 # потому что нумеруем остановки с нуля


assert solution(5, 2, 4, 1, (0, 2, 4, 6)) == 3
assert solution(1, 1, 100000, 100000, (0, 100000)) == 2
assert solution(1, 1, 2, 0, (0, 1, 2)) == 3

_, vb, vs = map(int, input().strip().split())
stops = tuple(map(int, input().strip().split()))
ux, uy = map(int, input().strip().split())
print(solution(vb, vs, ux, uy, stops))