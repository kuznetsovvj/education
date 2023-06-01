# https://codeforces.com/contest/1837/problem/A

def check(x, n):
    if x % n != 0:
        print("1", x, sep='\n')
    else:
        print("2", f"{x-1} 1", sep='\n')
        

for _ in range(int(input())):
    check(*map(int, input().split()))