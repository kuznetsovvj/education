#  https://codeforces.com/contest/1551/problem/D2
#  2100
#  c четвертой попытки - много ошибок в коэффициентах при show


import sys


def solution(a, b, k):
    # если всю площадь можно разбить на квадраты 2x2
    if a % 2 == 0 and b % 2 == 0:
        if k % 2 == 0 and k >= 0 and k <= a*b // 2:
            print("YES")
            show(a, b, k)
            return
        else:
            print("NO")
            return
    # если остается горизонтальная полоса
    if a % 2 == 1:
        if k >= b // 2 and k <= a*b//2 and (k - b//2) % 2 == 0:
            print("YES")
            show(a, b, k)
            return
        else:
            print("NO")
            return
    if b % 2 == 1:
        if k >= 0 and k <= a*(b-1)//2 and k % 2 == 0:
            print("YES")
            show(a, b, k)
            return
        else:
            print("NO")
            return

schemas = {0:{0:("a", "b"), 1:("c", "d"), 2:("e", "f")}, 1:{0:("g", "h"), 1:("k", "l"), 2:("m", "n")}, 2:{0:("o", "p"), 1:("r", "s"), 2:("t", "u")}}

def show(a, b, k):
    if a % 2 == 0:
        hor = k // 2
    else:
        hor = (k // 2) - (b // 4)
    for i in range(a//2):
        line1, line2 = "", ""
        for j in range(b//2):
            if hor > 0:
                line1 += f"{schemas[i%3][j%3][0]}{schemas[i%3][j%3][0]}"
                line2 += f"{schemas[i%3][j%3][1]}{schemas[i%3][j%3][1]}"
                hor -= 1
            else:
                line1 += f"{schemas[i%3][j%3][0]}{schemas[i%3][j%3][1]}"
                line2 += f"{schemas[i%3][j%3][0]}{schemas[i%3][j%3][1]}"
        if b % 2 != 0:
            line1 += f"{schemas[i%3][(b//2+1)%3][0]}"
            line2 += f"{schemas[i%3][(b//2+1)%3][0]}"
        print(line1)
        print(line2)
    if a % 2 != 0:
        line1 = ""
        for j in range(b//2):
            line1 += f"{schemas[(a//2+1)%3][j%3][0]}{schemas[(a//2+1)%3][j%3][0]}"
        print(line1)
    

inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for idx in range(1, len(inp)):
    solution(*inp[idx])
    