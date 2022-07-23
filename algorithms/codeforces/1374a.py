def solution(x, y, n):
    current = n % x # 0.. x-1
    if y <= current:
        print(n - current + y)
        return
    else:
        print(n - current - x + y)


inp = int(input())
for _ in range(inp):
    x, y, n = tuple(map(int, input().split()))
    solution(x, y, n)