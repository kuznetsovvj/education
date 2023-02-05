# https://codeforces.com/contest/1791/problem/E

def check(seq):
    # жадность не проходит (контр-пример [10, -3, -7, -5, -2])
    # последовательная обратка "выгодно/невыгодно" не проходит (контр-пример [10, -1, -7, -6, 3])

    # наркомания на марше:
    # если кол-во отрицательных чисел четное, то мы сможем сделать все числа четными
    # если нечетное - то одно чисел в массиве останется отрицательным (или нулем)

    nn, s, m = 0, 0, abs(seq[0])
    for item in seq:
        if item < 0:
            nn += 1
        s += abs(item)
        m = min(m, abs(item))
    
    if nn % 2 == 0:
        return s
    else:
        return s - (m * 2)

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))