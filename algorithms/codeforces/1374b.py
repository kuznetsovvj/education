def solution(x):
    cnt = 0
    current = 1
    while True:
        if current < x:
            current *= 6
        elif current > x:
            if current % 2 == 0:
                current /= 2
            else:
                print("-1")
                return
        else:
            print(cnt)
            return
        cnt += 1


inp = int(input())
for _ in range(inp):
    x = int(input())
    solution(x)