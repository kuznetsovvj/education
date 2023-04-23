# https://codeforces.com/contest/1385/problem/C

# основная идея из подсказки (сам не догнал)
def check(seq):
    up = True
    for i in range(len(seq)-1, 0, -1):
        if up:
            if seq[i] <= seq[i-1]:
                continue
            else:
                up = False
        else:
            if seq[i] >= seq[i-1]:
                continue
            else:
                return i
    return 0


for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))