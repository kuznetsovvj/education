# https://codeforces.com/problemset/problem/1296/B

def check(n):
    res = n
    while n >= 10:
        k = n % 10
        n = n // 10
        res += n
        n = n + k
        
    return res
        

for _ in range(int(input())):
    print(check(int(input())))