import sys

def sol(x, y):
    if y % x == 0:
        b = y // x
        a = 1
        return f"{a} {b}"
    return "0 0"


p = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(p)):
    print(sol(*p[i]))