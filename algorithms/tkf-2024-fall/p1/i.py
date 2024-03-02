n = int(input())
cmd = tuple(map(int, input().split()))

def check(n, cmd):
    l = [0 for _ in range(n)]
    ans = [0 for _ in range(n+1)]
    ans[0] = 1
    i = 1
    start = len(l) - 1
    for c in cmd:
        if i == len(ans) - 1:
            ans[i] = 1
            break
        l[c-1] = 1
        # если мы не трогали самый правый ноль, то могла только увеличиться сумма на 1
        if c-1 != start:
            ans[i] = ans[i-1] + 1
            i += 1
        else:
        # если мы тронули самый правый ноль, то надо найти новый ноль
            j = start
            r = 0
            while l[j] != 0 and j > 0:
                r += 1
                j -= 1
            start = j
            ans[i] = ans[i-1] - r + 1
            i += 1
             
    return ' '.join(map(str, ans))

print(check(n, cmd))