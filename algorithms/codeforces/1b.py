# https://codeforces.com/contest/1/problem/B

import sys

def solution(w):
    idx, digit = [w[0]], False
    for i in range(1,len(w)):
        if w[i].isdigit():
            if not digit:
                idx.append(w[i])
                digit = True
            else:
                idx[-1] += w[i]
        else:
            if digit:
                idx.append(w[i])
                digit = False
            else:
                idx[-1] += w[i]
    if len(idx) == 2:
        # из ZZZ16
        res, t = 0, 0
        for r in idx[0][::-1]:
            res += (ord(r) - 64) * (26**t)
            t += 1
        return f"R{idx[1]}C{res}"
    else:
        # R25C237
        num = int(idx[3]) # число, которое надо перевести в буквенную систему
        # определим, сколько знаков-букв будет в результирующем числе
        reg, base = 1, 26
        while num > base:
            num -= base
            base *= 26
            reg += 1
        # reg - сколько знаков получившемся числе
        # num - число, которое нужно перевести в 26-ричную систему счисления

        res = []
        num -= 1
        while num >= 26:
            res.append(num % 26)
            num = num // 26
        res.append(num % 26)
        res = res[::-1]
        if len(res) < reg:
            res = [0] * (reg - len(res)) + res
        s = ""
        for i in res:
            s += chr(i + 65)
        return f"{s}{idx[1]}"


inp = [line.strip() for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(inp[i]))