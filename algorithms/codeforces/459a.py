# https://codeforces.com/problemset/problem/459/A

def check(x1, y1, x2, y2):
    # дали две точки по вертикали
    if x1 == x2:
        x3 = x1 + max(y1, y2) - min(y1, y2)
        if x3 > 1000:
            x3 = x1 - max(y1, y2) + min(y1, y2)
            if x3 < -1000:
                return -1
        return f"{x3} {y1} {x3} {y2}"
    # дали две точки по горизонтали
    if y1 == y2:
        y3 = y1 + max(x1, x2) - min(x1, x2)
        if y3 > 1000:
            y3 = y1 - max(x1, x2) + min(x1, x2)
            if y3 < -1000:
                return -1
        return f"{x1} {y3} {x2} {y3}"

    # дали точки по диагонали
    if abs(x1 - x2) != abs(y1 - y2):
        # не квадрат
        return -1
    
    return f"{x1} {y2} {x2} {y1}"


x1, y1, x2, y2 = map(int, input().split())
print(check(x1, y1, x2, y2))

