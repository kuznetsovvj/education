# https://codeforces.com/contest/1834/problem/C

def check(w1, w2):
    fw, bc = 0, 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            fw += 1
        if w1[i] != w2[-1-i]:
            bc += 1
# 0: fw = 0
# 1: fw = 1
# 2: bc = 1
# 3: bc = 2
# 4: fw = 2
# 5: fw = 3
# 6: bc = 3
# 7: bc = 4
# 8: fw = 4
# 9: fw = 
    if fw == 0:
        return 0
    if bc == 0:
        return 2
    r_fw = fw * 2 - (fw % 2 == 1)
    r_bc = bc * 2 - (bc % 2 == 0)
    return min(r_fw, r_bc) 


for _ in range(int(input())):
    input()
    print(check(input(), input()))