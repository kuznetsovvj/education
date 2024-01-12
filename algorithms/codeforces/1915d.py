# https://codeforces.com/contest/1915/problem/D

gs = {'a', 'e'}

def check(s):
    res = []
    j = len(s) - 1
    while j >= 0:
        if s[j] in gs:
            res.append(s[j])
            res.append(s[j-1])
            res.append('.')
            j -= 2
        else:
            res.append(s[j])
            res.append(s[j-1])
            res.append(s[j-2])
            res.append('.')
            j -= 3
    del res[-1]
    return ''.join(res[::-1])       
        

for _ in range(int(input())):
    input()
    print(check(input()))