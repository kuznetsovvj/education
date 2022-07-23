# https://codeforces.com/contest/1650/problem/B

def solution(l, r, a):
    div_min = l // a
    div_max = r // a
    if div_max > div_min:
        return max(div_max + a - 2, div_max + (r % a))
    else:
        return div_max + (r % a)


k = int(input())
for _ in range(k):
    l, r, a = map(int, input().strip().split())
    print(solution(l, r, a))


assert solution(1, 4, 3) == 2
assert solution(5, 8, 4) == 4
assert solution(6, 10, 6) == 5
assert solution(10, 12, 8) == 5
assert solution(1, 1000000000, 1000000000) == 999999999