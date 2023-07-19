# https://codeforces.com/contest/1843/problem/B

def check(seq):
    res_s, res_t = 0, 0
    negative = False
    for i in seq:
        res_s += abs(i)
        if i < 0:
            if not negative:
                negative = True
                res_t += 1
        if i > 0:
            if negative:
                negative = False
    return f"{res_s} {res_t}"                
    

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))