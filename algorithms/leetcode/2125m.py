# https://leetcode.com/problems/number-of-laser-beams-in-a-bank

def nubmerOfBeams(bank):
    res = 0
    cur = 0
    for line in bank:
        t = 0
        for item in line:
            if item == '1':
                t += 1
        if cur == 0:
            cur = t
        else:
            if t != 0:
                res += t * cur
                cur = t
    return res

assert nubmerOfBeams(bank = ["011001","000000","010100","001000"]) == 8
assert nubmerOfBeams(bank = ["000","111","000"]) == 0